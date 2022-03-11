from valetapp.views.Command.command import Command


class PendingCommand(Command):
    def __init__(self, name, booking) -> None:
        super().__init__()
        self.name = name
        self.booking = booking

    def execute(self) -> None:
        self.booking.pending()
        self.booking.save()
