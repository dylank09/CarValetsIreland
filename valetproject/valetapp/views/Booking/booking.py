from django.views.generic import ListView
from django.shortcuts import render
from valetapp.models.Store.chainstore import ChainStore
from valetapp.models.Booking.booking import Booking
from valetapp.models.Valet.valetservice import CompositeBaseValet, CompositeExterior, Wash, Wax, Polish, CompositeInterior, SteamClean, Vacuum, Leather
from valetapp.models.Users.customer import Customer
from valetapp.forms.Booking.bookService import AvailabilityForm
from valetapp.views.Builder.goldBuilder import GoldBuilder
from valetapp.views.Builder.bronzeBuilder import BronzeBuilder
from valetapp.views.Builder.silverBuilder import SilverBuilder
from valetapp.views.addOns import ConcreteValet, WaxCost, WashCost, PolishCost, LeatherCost, SteamCleanCost, VacuumCost
import math
from datetime import datetime, timedelta
import pytz
from valetapp.framework.concreteFramework import concreteFramework
from valetapp.interceptor.concreteInterceptor1 import concreteInterceptor1
from valetapp.interceptor.concreteInterceptor2 import concreteInterceptor2


utc = pytz.UTC


class BookingList(ListView):
    model = Booking
    context_object_name = 'obj'
    template_name = 'Booking/booking_list.html'


def closest_avail_store(store, long, lat, start_time, stores_to_exclude):

    stores = ChainStore.objects.exclude(name=store)
    for store2 in stores_to_exclude:
        stores = stores.exclude(name=store2)

    closest_store = stores[0]

    X = closest_store.get_longitude() - long
    Y = closest_store.get_latitude() - lat

    closest_store_distance = distance_to_store(X, Y)

    for store in stores:
        X = store.get_longitude() - long
        Y = store.get_latitude() - lat
        distance_to_current = distance_to_store(X, Y)

        if(distance_to_current < closest_store_distance):
            closest_store = store

    store_max = closest_store.get_max_valets_per_hour()
    storeid = ChainStore.objects.filter(name=closest_store.get_name())[0]

    bookings = Booking.objects.filter(store=storeid, start_time=start_time)

    if (len(bookings) <= store_max):
        return closest_store

    stores_to_exclude.append(closest_store)
    return closest_avail_store(
        store, X, Y, start_time, stores_to_exclude)


def distance_to_store(x, y):
    return math.sqrt(math.pow(x, 2) + math.pow(y, 2))


def check_booking_availability(store_name, storeid, start_time):

    store = ChainStore.objects.get(name=store_name)
    store_max = store.get_max_valets_per_hour()

    bookings = Booking.objects.filter(store=storeid, start_time=start_time)

    store_long = store.get_longitude()
    store_lat = store.get_latitude()

    if (len(bookings) > store_max):

        stores_to_exclude = [store]
        tempstore = closest_avail_store(
            store, store_long, store_lat, start_time, stores_to_exclude)
        return tempstore
    else:
        return store


def init_booking_form(request):
    if request.method == 'POST':
        form = AvailabilityForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            return create_booking(request, data)
    else:
        form = AvailabilityForm()
    return render(request, 'Booking/bookingservice_form.html', {'form': form})


def create_booking(request, data):

    valet_services = data['valet_services']

    base, total_booking_cost, valets = get_valet_services(valet_services)

    booking_duration = base.add_duration()
    booking_duration = timedelta(minutes=booking_duration)

    store_name = data['stores']
    storeid = ChainStore.objects.filter(name=data['stores'])[0]
    store = check_booking_availability(
        store_name, storeid, data['start_time'])
    storeid = ChainStore.objects.filter(name=store.get_name())[0]

    num_bookings = Booking.objects.count()

    if len(valet_services) > 0:  # precondition
        req = make_booking(request, data, total_booking_cost,
                           valets, booking_duration, storeid)

    num_bookings_after = Booking.objects.count()

    if num_bookings_after > num_bookings:  # postcondition
        return req

    return ""


def get_valet_services(available_booking):

    base = CompositeBaseValet()
    ext_composite = CompositeExterior()
    int_composite = CompositeInterior()
    valet = ConcreteValet()
    valets = ""

    for v in available_booking:
        if v == "Leather":
            int_composite.add(Leather())
            valet = LeatherCost(valet)
        elif v == "Polish":
            ext_composite.add(Polish())
            valet = PolishCost(valet)
        elif v == "Steam":
            int_composite.add(SteamClean())
            valet = SteamCleanCost(valet)
        elif v == "Vacuum":
            int_composite.add(Vacuum())
            valet = VacuumCost(valet)
        elif v == "Wash":
            ext_composite.add(Wash())
            valet = WashCost(valet)
        elif v == "Wax":
            ext_composite.add(Wax())
            valet = WaxCost(valet)

        valets = v+","+valets

    total_booking_cost = valet.get_valet_cost()

    base.add(ext_composite)
    base.add(int_composite)

    return base, total_booking_cost, valets


def make_booking(request, data, total_booking_cost, valets, booking_duration, storeid):
    customer = Customer.objects.filter(user=request.user)[0]
    booking = Booking(
        user=customer,
        valetservice=valets,
        start_time=data['start_time'],
        end_time=data['start_time'] + booking_duration,
        price=total_booking_cost,
        store=storeid
    )

    booking.save()
    check_for_free_8th_booking(customer, booking)
    return pay_for_booking(request, booking)


def pay_for_booking(request, booking):

    customer = Customer.objects.filter(user=request.user)[0]

    old_price = (booking.get_price())

    booking.attach(customer)
    booking.notify()

    discount = old_price - booking.get_price()
    return render(request, "Booking/payForBooking.html", {'booking': booking, 'oldPrice': old_price, 'discount': discount})


def check_for_free_8th_booking(customer, booking):
    bookings = Booking.objects.filter(user=customer)
    number_of_bookings = len(bookings) % 8
    if number_of_bookings == 0:
        booking.set_price(0)


def confirm_pay(request, bookingid):
    booking = Booking.objects.filter(id=bookingid)[0]
    booking.book()
    booking.save()

    return render(request, 'Home/home.html')


def cancel_booking(request, bookingid):
    booking = Booking.objects.filter(id=bookingid)[0]
    now = datetime.now()
    if utc.localize(now-timedelta(hours=24)) <= booking.get_start_time() <= utc.localize(now+timedelta(hours=24)):
        print('error cannot cancel 24 hours before')
    else:
        booking.cancel()
        booking.save()

    return render(request, 'Home/home.html')


def view_user_bookings(request):
    customer = Customer.objects.filter(user=request.user)[0]
    bookings = Booking.objects.filter(user=customer)
    bookings = bookings.exclude(booking_state="CANCELLED")
    bookingID = []
    for booking in bookings:
        bookingID.append(booking.id)
    return render(request, 'Booking/cancel_list.html', {'bookings': bookings, 'bookingID': bookingID})


def builder(request):
    customer = Customer.objects.filter(user=request.user)[0]
    memberShip_Type = customer.getMemberShip_Type().get_colour()
    builder = {}
    if (memberShip_Type == "gold"):
        builder = GoldBuilder()
        builder.add_valet_service_a()
        builder.add_valet_service_b()
        builder.add_valet_service_c()

    if (memberShip_Type == "silver"):
        builder = SilverBuilder()
        builder.add_valet_service_a()
        builder.add_valet_service_b()
        builder.add_valet_service_c()

    if (memberShip_Type == "bronze"):
        builder = BronzeBuilder()
        builder.add_valet_service_a()
        builder.add_valet_service_b()
        builder.add_valet_service_c()

    product = builder.product
    print("Valets: ")
    print(product['valets'])
    print("Valet Cost: ")
    print(product['valet'].get_valet_cost())
    print("Valet Duration: ")
    print(product['duration'])
    return render(request, 'Booking/builder.html')


def interceptor(request):
    concreteFramework1 = concreteFramework()
    concreteInterceptorA = concreteInterceptor1()
    concreteInterceptorB = concreteInterceptor2()
    concreteFramework1.dispatcher.registerInterceptor(concreteInterceptorA)
    concreteFramework1.dispatcher.registerInterceptor(concreteInterceptorB)
    concreteFramework1.event()

    return render(request, 'Booking/interceptor.html')
