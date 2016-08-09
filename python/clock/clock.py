"""clock module to handle times without dates"""
from typing import Tuple

class Clock(object):
    """Class to handle times composed only by hours and minutes"""
    def _wrap_time(self, hour: int, minutes: int) -> Tuple[int, int]:
        """Wrap the hours and minutes to valid values"""
        new_minutes = minutes % 60
        new_hour = ( hour + minutes // 60 ) % 24
        return new_hour, new_minutes

    def __init__(self, hour: int, minutes: int) -> None:
        self.hour, self.minutes = self._wrap_time(hour, minutes)

    def __eq__(self, other: 'Clock') -> bool:
        return other.hour == self.hour and other.minutes == self.minutes

    def __str__(self) -> str:
        return '{:0>2d}:{:0>2d}'.format(self.hour, self.minutes)

    def add(self, minutes: int) -> 'Clock':
        """Adds minutes to the current time and return a new Clock object"""
        return Clock(self.hour, self.minutes + minutes)
