def is_leap_year(year: int) -> bool:
    """Determine if the given year is leap in the according to the Gregorian
    calendar.

    A leap year is a year evenly divisible by 4, except if it is divisible by
    100 but not by 400."""
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
