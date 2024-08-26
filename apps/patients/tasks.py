from celery import shared_task

from apps.patients.models import Room


@shared_task
def clear_expired_rooms_task():
    print('task worked')
    Room.objects.clear_expired_rooms()
