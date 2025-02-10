from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from datacenter.operations_with_time import get_duration, format_duration, is_visit_long


def storage_information_view(request):
    visits_not_leaved = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []

    for visit in visits_not_leaved:
        name = visit.passcard.owner_name
        entered_at = localtime(visit.entered_at)
        leaved_at = localtime(visit.leaved_at)
        duration = format_duration(duration=get_duration(leave=leaved_at, enter=entered_at))
        flag = is_visit_long(duration=get_duration(leave=leaved_at, enter=entered_at), minutes=60)

        person_info = {
            'who_entered': name,
            'entered_at': entered_at,
            'duration': duration,
            'is_strange': flag
        }

        non_closed_visits.append(person_info)

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
