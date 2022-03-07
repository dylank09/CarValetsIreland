from django.urls import path
from valetapp.views import views
from valetapp.views.Authentication import auth
from valetapp.views.Booking import booking
from valetapp.views.Visitor import exportToCSV
from valetapp.views.Visitor.CSVMaker import CSVMaker
from valetapp.views.Booking.booking import BookingList
from valetapp.views.Command import commandClient

urlpatterns = [
    path('', auth.register, name='index'),
    path('bookingservice_form/', booking.init_booking_form, name='BookingView'),
    path('booking_list/', BookingList.as_view(), name='BookingList'),
    path('payForBooking/<int:bookingId>',
         booking.pay_for_booking, name='payForBooking'),
    path('cancel_list/', booking.view_user_bookings, name='viewUsersBookings'),
    path('cancelBooking/<int:bookingid>',
         booking.cancel_booking, name='cancelBooking'),
    path('confirmBooking/<int:bookingid>',
         booking.confirm_pay, name='confirmPay'),
    path('register/', auth.register, name='register'),
    path('home/', views.home, name='home'),
    path('commands/', commandClient.commandClient, name='commandClient'),
    path('execute/<str:concreteCommandName>',
         commandClient.execute, name='execute'),
    path('view/', CSVMaker.get_emails, name='getVisitor'),
    path('login/', auth.login_page, name='loginUser'),
    path('logout/', auth.user_logout, name='logout'),
]
