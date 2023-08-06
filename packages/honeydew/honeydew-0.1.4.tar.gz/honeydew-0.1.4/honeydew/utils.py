import calendar
from datetime import datetime
class Utils:
    def __init__(self):
        """Instantiate utilities.
        """

def convert_dt_to_epoch(dt):
    """
    Convert datetime in UTC time zone to epoch (unix time)
    Args:
        dt (datetime): datetime
    Returns:
        result (int): epoch or unix time
    """
    return calendar.timegm(dt.utctimetuple())

def convert_epoch_to_dt(epoch):
    """
    Convert epoch to datetime
    Args:
        epoch (int): epoch or unix time
    Returns:
        result (datetime): datetime
    """
    if epoch > 9999999999:
        epoch = round(epoch/1000)
    return datetime.fromtimestamp(s)