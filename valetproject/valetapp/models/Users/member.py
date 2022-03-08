from abc import abstractmethod
from django.db import models
from valetapp.forms.Registration.Factory import Factory

class Member(models.Model):

    class Meta:
        abstract = True
        factory = None

    @abstractmethod
    def get_email(self):
        pass
    
    def create_user(self, user, colour):
        print(user)
        print(colour)
        self.factory().create_user(user=user, colour=colour)
