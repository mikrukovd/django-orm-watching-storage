from django.db import models
import datetime

SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )


def get_duration(leave, enter):
    if leave is None:
        leave = datetime.datetime.now()
    return (leave - enter)


def format_duration(duration):
    seconds = int(duration % SECONDS_IN_MINUTE)
    minutes = int((duration % SECONDS_IN_HOUR) // SECONDS_IN_MINUTE)
    hour = int(duration // SECONDS_IN_HOUR)
    return datetime.timedelta(hours=hour, minutes=minutes, seconds=seconds)


def is_visit_long(duration, hour):
    return duration > datetime.timedelta(hours=hour)
