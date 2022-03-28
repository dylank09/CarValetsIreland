from valetapp.models.Valet.valetservice import CompositeBaseValet, CompositeExterior, CompositeInterior, Vacuum, Wash, Wax
from valetapp.views.Builder.builder import Builder
from valetapp.views.addOns import ConcreteValet, VacuumCost, WashCost

class SilverBuilder(Builder):

    base = CompositeBaseValet()
    ext_composite = CompositeExterior()
    int_composite = CompositeInterior()
    valet = ConcreteValet()
    valets = ""

    def reset(self) -> None:
        self.valet = {}

    @property
    def product(self):

        # self.base.add(self.int_composite)
        # product = self.base
        product = {"valet":self.valet, "valets": self.valets}
        self.reset()
        return product

    def add_valet_service_a(self) -> None:
        self.int_composite.add(Vacuum())
        self.valet = VacuumCost(self.valet)
        self.valets = "Vacuum"+","+self.valets

    def add_valet_service_b(self) -> None:
        self.ext_composite.add(Wash())
        self.valet = WashCost(self.valet)
        self.valets = "Wash"+","+self.valets