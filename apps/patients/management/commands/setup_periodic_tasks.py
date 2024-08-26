from django.core.management.base import BaseCommand
from django_celery_beat.models import PeriodicTask, IntervalSchedule

class Command(BaseCommand):
    help = 'Set up periodic tasks for Celery'

    def handle(self, *args, **kwargs):
        # Define the interval schedule (e.g., every 2 hours)
        schedule, created = IntervalSchedule.objects.get_or_create(
            every=2,
            period=IntervalSchedule.HOURS,
        )
        PeriodicTask.objects.update_or_create(
            interval=schedule,
            name='Clear expired rooms',
            task='apps.patients.tasks.clear_expired_rooms_task',
        )

        self.stdout.write(self.style.SUCCESS('Successfully set up periodic tasks'))
