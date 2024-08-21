import uuid
from datetime import datetime as dt
from django.db import models


class Todo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(blank=True, null=True, max_length=400)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(blank=True, null=True, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-created_at"]
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

    def save(self, *args, **kwargs):
        if self.created_at == self.updated_at:
            self.start_time = dt.now()

        if self.status:
            self.end_time = dt.now()

        super().save(*args, **kwargs)
