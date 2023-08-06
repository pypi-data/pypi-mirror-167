"""Useful components related to asyncio, multithreading or multiprocessing."""
from __future__ import annotations

import asyncio
from contextlib import asynccontextmanager
from functools import partial, wraps
import logging
import threading
from typing import AsyncGenerator, Callable, Final, Optional, Protocol, TypeVar, Union

from typing_extensions import Concatenate, ParamSpec

from bitfount.config import _BITFOUNT_MULTITHREADING_DEBUG
from bitfount.exceptions import BitfountError

_logger = logging.getLogger(__name__)

_R = TypeVar("_R")
_P = ParamSpec("_P")

_DEFAULT_POLLING_TIMEOUT: Final = 5  # seconds


def asyncify(
    func: Callable[_P, _R], *args: _P.args, **kwargs: _P.kwargs
) -> asyncio.Future[_R]:
    """Run sync function in separate thread to avoid blocking event loop."""
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError as ex:
        raise BitfountError(
            "Tried to asyncify without running loop;"
            " asyncify() should only be called from async functions."
        ) from ex

    # Use default executor for this loop (signified by `None`)
    if kwargs:
        fut = loop.run_in_executor(None, partial(func, **kwargs), *args)
    else:
        # Separate this call version out, so we don't unnecessarily wrap in a partial
        # which makes debugging harder
        fut = loop.run_in_executor(None, func, *args)
    return fut


async def await_threading_event(
    event: threading.Event, timeout: Optional[float] = None
) -> bool:
    """Event.wait() that doesn't block the event loop."""
    return await asyncify(event.wait, timeout)


@asynccontextmanager
async def asyncnullcontext() -> AsyncGenerator[None, None]:
    """Async version of contextlib.nullcontext()."""
    yield None


@asynccontextmanager
async def async_lock(
    lock: threading.Lock,
    lock_name: str,
    polling_timeout: Optional[int] = _DEFAULT_POLLING_TIMEOUT,
) -> AsyncGenerator[None, None]:
    """Acquire a threading Lock without blocking the async event loop."""
    if _BITFOUNT_MULTITHREADING_DEBUG and polling_timeout is None:
        _logger.warning(
            f"async_lock({lock_name}) called without polling timeout for {lock=};"
            f" this may cause hanging threads"
        )

    acquired = False
    try:
        while True:
            if _BITFOUNT_MULTITHREADING_DEBUG:
                _logger.debug(f"Going to wait in thread on lock {lock_name} {lock=}")

            if polling_timeout is not None:
                acquired = await asyncify(lock.acquire, timeout=polling_timeout)
            else:
                acquired = await asyncify(lock.acquire)

            if acquired:
                if _BITFOUNT_MULTITHREADING_DEBUG:
                    _logger.info(f"Acquired lock {lock_name} {lock=}")
                break
            else:
                if _BITFOUNT_MULTITHREADING_DEBUG:
                    _logger.debug(
                        f"Didn't acquire lock {lock_name} {lock=} in timeout,"
                        f" will try again"
                    )

        yield  # the lock is held
    except asyncio.CancelledError as ce:
        if _BITFOUNT_MULTITHREADING_DEBUG:
            _logger.warning(
                f"Async lock {lock_name} was cancelled {acquired=} {lock=};"
                f" this may leave threads hanging if no timeout was specified"
            )
        raise ce
    finally:
        if acquired:
            if _BITFOUNT_MULTITHREADING_DEBUG:
                _logger.info(f"Releasing lock {lock_name} {lock=}")
            lock.release()


class ThreadWithException(threading.Thread):
    """A thread subclass that captures exceptions to be reraised in the main thread."""

    def run(self) -> None:
        """See parent method for documentation.

        Captures exceptions raised during the run call and stores them as an attribute.
        """
        self._exc: Optional[Exception] = None
        try:
            super().run()
        except Exception as e:
            self._exc = e
            raise e

    def join(self, timeout: Optional[float] = None) -> None:
        """See parent method for documentation.

        If an exception occurs in the joined thread it will be reraised in the calling
        thread.
        """
        super().join(timeout)
        if self._exc:
            raise self._exc


def wait_for_event_with_stop(
    wait_event: threading.Event,
    stop_event: threading.Event,
    polling_timeout: int = _DEFAULT_POLLING_TIMEOUT,
) -> None:
    """Helper function that waits on an event but allows exiting early.

    Monitors the wait_event but with a timeout, so it can periodically check if it
    should stop early.
    """
    while not stop_event.is_set():
        wait_event.wait(timeout=polling_timeout)
        if wait_event.is_set():
            return


# #################################################### #
# Decorator for thread-safe synchronisation of methods #
# #################################################### #
_LOCK = TypeVar("_LOCK", bound=Union[threading.Lock, threading.RLock])


class _Synchronisable(Protocol[_LOCK]):
    """Represents a class that can be synchronised."""

    _sync_lock: _LOCK


SelfWithLock = TypeVar(
    "SelfWithLock",
    bound=Union[_Synchronisable[threading.Lock], _Synchronisable[threading.RLock]],
)


def _synchronised(
    meth: Callable[Concatenate[SelfWithLock, _P], _R]
) -> Callable[Concatenate[SelfWithLock, _P], _R]:
    """Wrap target method with instance's Lock."""

    @wraps(meth)
    def _wrapper(self_: SelfWithLock, *args: _P.args, **kwargs: _P.kwargs) -> _R:
        if _BITFOUNT_MULTITHREADING_DEBUG:
            _logger.debug(
                f"Waiting on {self_.__class__.__name__} lock ({id(self_._sync_lock)})"
                f" in {threading.current_thread().name}"
            )

        with self_._sync_lock:
            if _BITFOUNT_MULTITHREADING_DEBUG:
                _logger.debug(
                    f"Got {self_.__class__.__name__} lock ({id(self_._sync_lock)}) in"
                    f" {threading.current_thread().name}"
                )

            res = meth(self_, *args, **kwargs)

        if _BITFOUNT_MULTITHREADING_DEBUG:
            _logger.debug(
                f"Released {self_.__class__.__name__} lock ({id(self_._sync_lock)}) in"
                f" {threading.current_thread().name}"
            )
        return res

    return _wrapper
