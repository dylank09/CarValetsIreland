from valetapp.models.Valet.valetservice import CompositeBaseValet, CompositeExterior, CompositeInterior, Leather, Polish, Wash
from valetapp.views.Builder.builder import Builder
from valetapp.views.addOns import ConcreteValet, LeatherCost, WashCost, PolishCost


class SilverBuilder(Builder):

    base = CompositeBaseValet()
    ext_composite = CompositeExterior()
    int_composite = CompositeInterior()
    valet = ConcreteValet()
    valets = ""

    def reset(self) -> None:
        self.valet = {}
        self.valets = {}
        self.base = CompositeBaseValet()

    @property
    def product(self):
        self.base.add(self.ext_composite)
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
        self.ext_composite.add(Wash())
        self.valet = WashCost(self.valet)
        self.valets = "Wash"+","+self.valets

    def add_valet_service_c(self) -> None:
        self.int_composite.add(Polish())
        self.valet = PolishCost(self.valet)
        self.valets = "Polish"+","+self.valets
