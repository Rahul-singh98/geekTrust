from .constants import *
from datetime import datetime , timedelta
from dateutil.relativedelta import relativedelta

class Subscriptions(object):

    def __init__(self ):
        self.subscription_date = None
        self.total_amount = 0
        self.isTopedUp = False 
        self.output = []
        self.subscribed_channels = set()

    def stringToDatetime(self, date:str) -> str:
        try:
            self.subscription_date = datetime.strptime(date, DATE_FORMAT)
            return VALID_DATE
        except:
            return self.printAndReturn(INVALID_DATE)

    def add_subscription(self, category:str, plan_name:str) -> str:
        if self.subscription_date is not None:
            if category not in self.subscribed_channels:
                self.subscribed_channels.add(category)
                self.total_amount += SUBSCRIPTION_PLANS[category][plan_name]
                if plan_name == PREMIUM:
                    expiry = self.get_expiry_date(PREMIUM_DURATION)
                else:
                    expiry = self.get_expiry_date(BASE_DURATION)

                self.output.append(f"{RENEWAL_REMINDER} {category} {expiry}")
                return VALID
            return self.printAndReturn(DUPLICATE_CATEGORY)
        return self.printAndReturn(SUBSCRIPTION_INVALID_DATE)

    def add_topup(self, category, duration):
        if self.subscription_date is None:
            return self.printAndReturn(TOPUP_INVALID_DATE)
            
        if len(self.subscribed_channels) !=0:
            if(not self.isTopedUp):
                self.isTopedUp = True
                self.total_amount+= TOPUP_PLANS[category] * duration
                return VALID
            return self.printAndReturn(DUPLICATE_TOPUP)
        return self.printAndReturn(TOPUP_NO_SUSCRIPTION)

    def print_renewal_details(self ):
        if len(self.subscribed_channels) == 0:
            return self.printAndReturn(SUBSCRIPTIONS_NOT_FOUND)
    
        for output in self.output:
            print(output)
        print(f"{RENEWAL_AMOUNT} {self.total_amount}")
        return None

    def get_expiry_date(self, months):
        date = self.subscription_date \
               + relativedelta(months=months) \
               - timedelta(REMINDER_DAYS)

        return date.strftime(DATE_FORMAT)

    def printAndReturn(self, msg):
        print(msg)
        return msg