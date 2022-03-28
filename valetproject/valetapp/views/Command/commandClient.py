from valetapp.models.Booking.booking import Booking
from valetapp.views.Command.cancelCommand import CancelCommand
from valetapp.views.Command.bookCommand import BookCommand
from valetapp.views.Command.pendingCommand import PendingCommand
from django.shortcuts import render

# booking = Booking.objects.filter()[0]
# cancelCommand = CancelCommand("cancel", booking)
# bookCommand = BookCommand("book", booking)
# pendingCommand = PendingCommand("pending", booking)
# commandsMap = dict({"cancel": cancelCommand,
#                    "book": bookCommand, "pending": pendingCommand})


def commandClient(request):
    return render(request, "Command/commandClient.html", {"cancelCommand": cancelCommand.name, "bookCommand": bookCommand.name, "pendingCommand": pendingCommand.name})


def execute(request, concreteCommandName):
    conncreteCommand = commandsMap[concreteCommandName]
    conncreteCommand.execute()

    return render(request, 'Home/home.html')
