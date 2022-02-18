from django.db import models
from django.contrib.auth.models import User
import uuid


class Staff(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    staffId = models.UUIDField(
        max_length=100, blank=True, unique=True, default=uuid.uuid4)

    def get_staff_email(self):
        return self.user.email

    def accept(self, visitor):
        return visitor.visit(self)
        