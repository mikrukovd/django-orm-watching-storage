from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime
from datacenter.models import get_duration, format_duration, is_visit_long


def passcard_info_view(request, passcode):
    this_passcard_visits = []
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)

    for visit in visits:
        enter = localtime(visit.entered_at)
        leave = localtime(visit.leaved_at)
        duration = get_duration(enter=enter, leave=leave)
        flag = is_visit_long(duration=duration)
        duration = format_duration(duration=duration)
        visit_data = {
            'entered_at': enter,
            'duration': duration,
            'is_strange': flag
        }
        this_passcard_visits.append(visit_data)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }

    return render(request, 'passcard_info.html', context)
