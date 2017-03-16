from datetime import datetime

def days_to_ny():
    now = datetime.now()
    ny_date= datetime(now.year + 1, 1, 1)
    delta = (ny_date- now).days
    return delta

print('До нового года осталось {} дней'.format(days_to_ny()))