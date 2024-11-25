from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "api"

    def ready(self):
        from django_celery_beat.models import IntervalSchedule, PeriodicTask # noqa: F401, I001
        self.add_periodic_task()

    def add_periodic_task(self):
        from api.tasks import sync_cache_to_db  # noqa: F401, I001
        from django_celery_beat.models import IntervalSchedule, PeriodicTask

        schedule, created = IntervalSchedule.objects.get_or_create(
            every=1,
            period=IntervalSchedule.HOURS,
        )

        PeriodicTask.objects.get_or_create(
            interval=schedule,
            name="sync cache data to the database",
            task="api.tasks.sync_cache_to_db",

        )


