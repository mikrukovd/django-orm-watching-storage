import datetime

SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60


def get_duration(leave, enter):
    leave = leave or datetime.datetime.now()
    return (leave - enter).total_seconds()


def format_duration(duration):
    seconds = int(duration % SECONDS_IN_MINUTE)
    minutes = int((duration % SECONDS_IN_HOUR) // SECONDS_IN_MINUTE)
    hours = int(duration // SECONDS_IN_HOUR)
    return datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)


def is_visit_long(duration, hour):
    return duration > datetime.timedelta(hours=hour)
