from valetapp.models.Valet.valetservice import CompositeBaseValet, CompositeExterior, CompositeInterior, Leather, Vacuum, SteamClean
from valetapp.views.Builder.builder import Builder
from valetapp.views.addOns import ConcreteValet, LeatherCost, VacuumCost, SteamCleanCost


class BronzeBuilder(Builder):

    base = CompositeBaseValet()
    int_composite = CompositeInterior()
    valet = ConcreteValet()
    valets = ""

    def reset(self) -> None:
        self.valet = {}
        self.valets = {}
        self.base = CompositeBaseValet()

    @property
    def product(self):
        self.base.add(self.int_composite)
        self.base = self.base.add_duration()
        product = {"valet": self.valet,
                   "valets": self.valets, "duration": self.base}
        self.reset()
        return product

    def add_valet_service_a(self) -> None:
        self.int_composite.add(Leather())
        self.valet = LeatherCost(self.valet)
        self.valets = "Leather"+","+self.valets

    def add_valet_service_b(self) -> None:
        self.int_composite.add(Vacuum())
        self.valet = VacuumCost(self.valet)
        self.valets = "Vacuum"+","+self.valets

    def add_valet_service_c(self) -> None:
        self.int_composite.add(SteamClean())
        self.valet = SteamCleanCost(self.valet)
        self.valets = "Steam"+","+self.valets
