from datetime import datetime

def unixtime_date(input):
    """
    TODO:
    Convert a Unix timestamp into a readable date and time string.
    Expected format: YYYY-MM-DD HH:MM:SS

    -------------------------------------------------------------------------
    HOW THE INPUT BECOMES THE OUTPUT
    -------------------------------------------------------------------------

    Step 1 - What is a Unix timestamp?
        It is a single number: the count of seconds elapsed since the
        "Unix epoch" -- 1970-01-01 00:00:00 UTC.
        Example: 1700000000 means "1.7 billion seconds after 1 Jan 1970".
        Computers love it because it's just an integer/float, easy to
        store and sort.

            input = 1700000000   <- just a number, no human meaning yet

    Step 2 - Turn the number into a datetime OBJECT
            dt = datetime.fromtimestamp(input)

        - `datetime` is a CLASS imported from the `datetime` module
          (see the `from datetime import datetime` line at the top).
        - `.fromtimestamp(...)` is a CLASS METHOD that takes a Unix
          timestamp and returns a `datetime` object -- Python's
          structured representation of a calendar date AND time of day.
        - Internally it counts forward from the epoch and works out the
          year, month, day, hour, minute, second (in your local timezone).

            dt  ->  datetime(2023, 11, 14, 22, 13, 20)
                    (year,  month, day, hour, minute, second)

        It is still NOT a string -- it's an object you can do calendar
        maths on (e.g. add days, compare two dates).

    Step 3 - Format the object as TEXT
            return dt.strftime("%Y-%m-%d %H:%M:%S")

        - strftime = "string format time". It takes a datetime and
          returns a string, using format codes (the `%` parts).
        - Each %X is a placeholder the method fills in:

            %Y  4-digit year                 e.g. 2023
            %m  2-digit month  (01-12)       e.g. 11
            %d  2-digit day    (01-31)       e.g. 14
            %H  2-digit hour, 24-h (00-23)   e.g. 22
            %M  2-digit minute (00-59)       e.g. 13
            %S  2-digit second (00-59)       e.g. 20

        - The literal "-", " " (space), and ":" are kept exactly as
          written. So "%Y-%m-%d %H:%M:%S" becomes "2023-11-14 22:13:20".

    -------------------------------------------------------------------------
    PIPELINE PICTURE
    -------------------------------------------------------------------------
        1700000000
            |
            v   datetime.fromtimestamp(...)
        datetime(2023, 11, 14, 22, 13, 20)
            |
            v   .strftime("%Y-%m-%d %H:%M:%S")
        "2023-11-14 22:13:20"

    -------------------------------------------------------------------------
    EXAMPLES
    -------------------------------------------------------------------------
        unixtime_date(0)            -> "1970-01-01 07:30:00"  (in SGT,
                                       because fromtimestamp uses local time)
        unixtime_date(1700000000)   -> "2023-11-14 22:13:20"  (in SGT)
        unixtime_date(1000000000)   -> "2001-09-09 09:46:40"

    -------------------------------------------------------------------------
    SMALL GOTCHAS
    -------------------------------------------------------------------------
    1. TIMEZONES
       `fromtimestamp` uses your LOCAL timezone, so the same number gives
       a different string in Singapore vs London. For UTC use
       `datetime.utcfromtimestamp(input)` instead.

    2. SHADOWING `input`
       Naming the parameter `input` overrides Python's built-in `input()`
       function inside this function. It's harmless here, but in larger
       code you'd usually call it `ts` or `timestamp`.
    """
    # Write your code here
    pass




