"""Run a python script or function only once in a given time frame."""

import datetime
import functools
import logging
import pathlib
import pickle
import typing

import appdirs

__version__ = "1.0.0"


STATE_DIR = pathlib.Path(appdirs.user_state_dir("once_only", "mikapfl"))


class Once:
    """Class for time keeping, enabling you to run functions only once in a given
    time span."""

    def __init__(
        self,
        timedelta: datetime.timedelta,
        file: typing.Union[pathlib.Path, None] = None,
    ):
        if file is None:
            microseconds = int(
                round(timedelta.total_seconds() * 1000 * 1000 + timedelta.microseconds)
            )
            file = STATE_DIR / f"timestamp_{microseconds:d}.pck"
        self.file = file
        self.timedelta = timedelta
        self.last_trigger_time = self._read_last_trigger_time()

    def _read_last_trigger_time(self) -> datetime.datetime:
        """Read the last time the time interval was triggered from the backing file."""
        try:
            with self.file.open("rb") as fd:
                return pickle.load(fd)
        except IOError:
            logging.debug(
                f"No database for timedelta {self.timedelta} found, using 1.1.1970"
            )
            return datetime.datetime.fromtimestamp(0)

    def check_ready(self) -> bool:
        """Check if the last execution was longer ago than the timedelta.

        Returns True if the last execution was longer ago, False otherwise.
        Does not record a new execution."""
        now = datetime.datetime.now()
        return (now - self.last_trigger_time) >= self.timedelta

    def check_ready_trigger(self) -> bool:
        """Check if the last execution was longer ago than the timedelta, and record
        a new execution.

        If the last execution was longer ago than the timedelta, return True and
        records a new execution now. Otherwise, returns False."""
        timedelta_passed = self.check_ready()
        if timedelta_passed:
            now = datetime.datetime.now()
            self._write_trigger_time(now)
            self.last_trigger_time = now
        return timedelta_passed

    def _write_trigger_time(self, time: datetime.datetime):
        """Write the give time to the backing file to record that it was triggered."""
        STATE_DIR.mkdir(parents=True, exist_ok=True)
        with self.file.open("wb") as fd:
            pickle.dump(time, fd)

    def __call__(self, func):
        """Act as a decorator on func, only running it at most once in the timedelta."""

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if self.check_ready_trigger():
                func(*args, **kwargs)

        return wrapper

    def __repr__(self):
        return (
            f"<Once timedelta={self.timedelta} last_trigger={self.last_trigger_time}>"
        )


weekly = Once(datetime.timedelta(7))
daily = Once(datetime.timedelta(1))
hourly = Once(datetime.timedelta(0, 60 * 60))
minutely = Once(datetime.timedelta(0, 60))
