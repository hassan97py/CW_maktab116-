from datetime import datetime, date, timedelta

class DateHelper:
    @classmethod
    def get_next_day(cls, date_obj):
        next_day_datetime = datetime(date_obj.year, date_obj.month, date_obj.day) + timedelta(days=1)
        return next_day_datetime.date()

today = date.today()
next_day = DateHelper.get_next_day(today)
print(f"today: {today}")
print(f"tommorow: {next_day}")