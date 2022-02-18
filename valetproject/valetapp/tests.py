from django.test import TestCase
from valetapp.forms.Registration.signup import SignUpForm
from django.urls import reverse
from django.contrib.auth.models import User
from valetapp.models.Users.customer import Customer
from valetapp.models.Users.membershiptype import MembershipType
from valetapp.models.Store.chainstore import ChainStore
from valetapp.models.Valet.valet import Valet


class signup_form_test(TestCase):

    def test_signup_labels(self):
        signup_form = SignUpForm()
        self.assertTrue(signup_form.fields['first_name'].label is None)
        self.assertTrue(signup_form.fields['last_name'].label is None)
        self.assertTrue(signup_form.fields['email'].label is None)

    def test_signup_success(self):
        user_data = {
            'username': 'dylank09',
            'first_name': 'Dylan',
            'last_name': 'Kearney',
            'email': 'dk@gmail.com',
            'password1': 'audi1234',
            'password2': 'audi1234',
        }
        signup_form = SignUpForm(user_data)
        self.assertTrue(signup_form.is_valid())
        user = signup_form.save()
        self.assertTrue(getattr(user, 'username'), 'dylank09')
        self.assertTrue(user.check_password('audi1234'))

    def test_signup_fail(self):
        user_data = {
            'username': '',
            'first_name': '',
            'last_name': '',
            'email': '',
            'password1': '',
            'password2': '',
        }
        form = SignUpForm(user_data)
        self.assertFalse(form.is_valid())

    def test_signup_password_empty(self):
        user_data = {
            'username': 'dylank123',
            'first_name': 'Dylan',
            'last_name': 'Kearney',
            'email': 'dk@mail.com',
            'password1': '',
            'password2': '',
        }
        form = SignUpForm(user_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form['password1'].errors, ['This field is required.'])
        self.assertEqual(form['password2'].errors, ['This field is required.'])


class login_test(TestCase):

    def test_login_page(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='login.html')

    def test_login_success(self):
        login_data = {
            'username': 'dylank09',
            'password': 'audi1234',
        }

        User.objects.create_user(**login_data)
        response = self.client.post(reverse('loginUser'), data={
            'username': login_data['username'],
            'password': login_data['password']
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.context['user']), 'dylank09')
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertRedirects(response, '../home/')

    def test_login_fail_on_username(self):
        login_data = {
            'username': 'dylank09',
            'password': 'audi1234',
        }

        User.objects.create_user(**login_data)
        response = self.client.post(reverse('loginUser'), data={
            'username': 'brokenName',
            'password': login_data['password']
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.context['user']), 'AnonymousUser')
        self.assertFalse(response.context['user'].is_authenticated)


class booking_test(TestCase):

    def test_booking_page(self):
        response = self.client.get('/bookingservice_form/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name='bookingservice_form.html')

    def test_booking_success(self):
        membershipType = {
            'colour': 'gold'
        }

        login_data = {
            'username': 'dylank09',
            'password': 'audi1234'
        }

        store_data = {
            'name': 'Tallaght',
            'longitude': 123,
            'latitude': 123,
            'rating': 5,
            'maxNumberOfValetsPerHour': 5
        }

        valet_data = {
            'name': 'Wash'
        }

        membershipType = MembershipType.objects.create(**membershipType)
        customer = User.objects.create_user(**login_data)
        store = ChainStore.objects.create(**store_data)
        store.save()
        stores = ChainStore.objects.all()
        valet = Valet.objects.create(**valet_data)
        valet.save()

        user_data = {
            'user': customer,
            'membershipType': membershipType
        }

        customer2 = Customer.objects.create(**user_data)

        response = self.client.post(reverse('loginUser'), data={
            'username': login_data['username'],
            'password': login_data['password']
        }, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.context['user']), 'dylank09')
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertRedirects(response, '../home/')
        valets = valet_data['name']

        response = self.client.post(reverse('BookingView'), data={
            'store': store.get_name(),
            'start_time': '2021-11-19 15:00:00+00:00',
            'valetservice': valet.get_name()
        }, follow=True)
        self.assertEqual(response.status_code, 200)
