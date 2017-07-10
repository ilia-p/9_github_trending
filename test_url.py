from datetime import date, timedelta

date_now = date.today()

delta_day = timedelta(days=1)
date_yesterday = date_now - delta_day

delta_week_ago = timedelta(days=7)
date_week_ago = date_now - delta_week_ago

print(date_now, date_yesterday, date_week_ago)

