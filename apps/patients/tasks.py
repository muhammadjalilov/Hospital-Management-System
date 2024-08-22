from django.utils import timezone

from apps.patients.models import Room


def clear_expired_rooms_task():
    with open('cron_log.txt', 'a') as log:
        log.write(f'crontab worked {timezone.now()}\n')
    Room.objects.clear_expired_rooms()