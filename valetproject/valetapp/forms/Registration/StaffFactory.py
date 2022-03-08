from valetapp.models.Users.staff import Staff
from .Factory import Factory

class StaffFactory(Factory):

    def create_user(self, user, colour=None):
        newuser = Staff(user=user)
        newuser.save()
        return newuser
