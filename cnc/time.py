import datetime

def get_current_time():
    now = datetime.datetime.now()
    clock = now.strftime("%H:%M")
    return clock

