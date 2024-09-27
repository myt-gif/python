import calendar
"""
    主要功能

    生成日历
    calendar.month(year, month)：以多行字符串的式形返回指定年份和月份的日历。例如，calendar.month(2024, 8)会打印出 2024 年 8 月的日历。
    calendar.prmonth(year, month)：直接打印指定年份和月份的日历到控制台。
    calendar.year(year)：以多行字符串的形式返回指定年份的全年日历。 //如果year无法使用  就用calendar.calender(year)
    判断闰年
    calendar.isleap(year)：判断指定的年份是否为闰年。如果是闰年，返回 True；否则返回 False。例如，2024 年是闰年，calendar.isleap(2024)将返回 True。
    判断闰年：能被 4 整除但不能被 100 整除的年份是闰年 / 能被 400 整除的年份也是闰年。
    获取日期信息
    calendar.weekday(year, month, day)：返回指定日期是星期几，其中星期一是 0，星期日是 6。例如，calendar.weekday(2024, 8, 29)表示 2024 年 8 月 29 日是星期四，所以返回值为 3。
    calendar.monthrange(year, month)：返回一个包含两个元素的元组，第一个元素是指定月份的第一天是星期几，第二个元素是指定月份的天数。例如，calendar.monthrange(2024, 8)返回 (3, 31)，表示 2024 年 8 月 1 日是星期四，这个月有 31 天。
"""

def display_cal(year_input, month_input):
    """
    Display a calendar for the desired year and month.

    Parameters:
    year_input (int): The year for which the calendar is to be displayed.
    month_input (int): The month for which the calendar is to be displayed.

    """
    print(calendar.month(year_input, month_input))


def fetch_year():
    """
    Prompts the user for a valid year and returns the year as an integer.
    """
    while True:
        try:
            year_input = int(input("Enter year: "))
            if year_input < 0:
                raise ValueError("Please enter a positive integer for the year.")
            return year_input
        except ValueError as e:
            print(e)


def fetch_month():
    """
    Function that asks the user to enter a month, validates the input, and returns the valid month.
    """
    while True:
        try:
            month_input = int(input("Enter month: "))
            if month_input < 1 or month_input > 12:
                raise ValueError("Please enter a number between 1 and 12 for the month.")
            return month_input
        except ValueError as e:
            print(e)


year_input = fetch_year()
month_input = fetch_month()

display_cal(year_input, month_input)