from abstract import IBillingStrategy
from rides.ride import ARide


class SimpleBilling(IBillingStrategy):
    
    def get_bill(self, ride: ARide):
        return super().get_bill(ride)
