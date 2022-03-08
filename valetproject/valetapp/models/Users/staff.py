from django.db import models
from django.contrib.auth.models import User
import uuid
from .member import Member


class Staff(models.Model, Member):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="valetapp.Staff.user+")
    staffId = models.UUIDField(
        max_length=100, blank=True, unique=True, default=uuid.uuid4)

    def get_email(self):
        return self.user.email

    def accept(self, visitor):
        return visitor.visit(self)
        