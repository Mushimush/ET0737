from datetime import datetime

def unixtime_date(input):
    """
    Convert a Unix timestamp into a readable date and time string.
    """
    dt = datetime.fromtimestamp(input)
    return dt.strftime("%Y-%m-%d %H:%M:%S")
