from valetapp.models.Users.membershiptype import MembershipType
from valetapp.models.Users.customer import Customer


class CustomerFactory():

    def create_user(self, user, colour):
        print(user)
        print(colour)
        
        newuser = Customer(user=user)
        membership_type_id = colour.index(')') - 1

        membership_type_id = colour[membership_type_id]
        colours = MembershipType.objects.filter(pk=membership_type_id)[0]

        # newuser.set_colour(colours)
        newuser.save()

        return newuser
