__author__ = "Shafikur Rahman"

from django.contrib.auth.models import AbstractUser
from django.db import models

from gist.models import Activity, TimeLog


class User(AbstractUser, TimeLog, Activity):
    email = models.EmailField(unique=True, blank=False, null=False)

    class Meta:
        app_label = "users"
        db_table = "bite_users"
        ordering = ["-add_at"]
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self):
        return self.username
