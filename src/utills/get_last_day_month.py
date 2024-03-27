import calendar

def get_last_day_of_month(year:int, month:int) -> int:
    """
    Get Last Day of Specific Month and Year
    """
    return calendar.monthrange(year, month)[1]