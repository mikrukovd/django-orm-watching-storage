from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime
from datacenter.operations_with_time import get_duration, format_duration, is_visit_long


def passcard_info_view(request, passcode):
    this_passcard_visits = []
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)

    for visit in visits:
        entered_at = localtime(visit.entered_at)
        leave_at = localtime(visit.leaved_at)
        duration = format_duration(duration=get_duration(enter=entered_at, leave=leave_at))
        flag = is_visit_long(duration=get_duration(enter=entered_at, leave=leave_at), minutes=60)

        visit_data = {
            'entered_at': entered_at,
            'duration': duration,
            'is_strange': flag
        }

        this_passcard_visits.append(visit_data)

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }

    return render(request, 'passcard_info.html', context)
