from datetime import timezone, timedelta

from django.db import models

from config.settings import AUTH_USER_MODEL
from users.models import User


class Wont(models.Model):
    owner = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="владелец",
    )
    place = models.CharField(max_length=100, verbose_name="Место")
    time = models.TimeField(default=timezone.now(), verbose_name="Время")
    action = models.CharField(max_length=100, verbose_name="Действие")
    is_pleasant = models.BooleanField(default=True, verbose_name="Признак приятной привычки")
    related_wont = models.ForeignKey('self', on_delete=models.SET_NULL, null=True,
                                     blank=True, verbose_name="Связанная привычка")
    period = models.PositiveIntegerField(verbose_name="Число поторений в неделю")
    award = models.CharField(max_length=100, null=True, blank=True, verbose_name="Вознаграждение")
    time_to_action = models.DurationField(default=timezone.timedelta(minutes=5), verbose_name="Время на выполнение")
    is_published = models.BooleanField(default=True, verbose_name="Признак публичности")

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"
