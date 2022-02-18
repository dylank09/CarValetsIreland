from django.db import models


class MembershipType(models.Model):
    colour = models.CharField(max_length=15)

    def get_colour(self):
        return self.colour

    def accept(self, visitor):
        return visitor.visit(self)

    class Meta:
        app_label = 'valetapp'
