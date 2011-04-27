from djangosanetesting.cases import *

from members.models import BidPolicy

from decimal import Decimal

from payments_dumpster.signals import free_quotes_payment_signal

from dumpster.models import MemberCompany, Region, MemberCompanyRegionBound, FreeQuotesRequest

from mockito import *

class TestSignalDispatchCase(DatabaseTestCase):
    fixtures = ['membercompanyregionbounds.json']

    def setUp(self):
        self.region = Region.objects.all()[0]
        self.mcrb = MemberCompanyRegionBound.objects.filter(region=self.region)[0]
        self.fqr = FreeQuotesRequest(company=self.mcrb.member_company)

    def test_quote_request(self):
      
        balance = self.mcrb.member_company.balance
        
        free_quotes_payment_signal.send(
            sender=self, 
            user_request_object=self.fqr, 
            region_bound=self.mcrb)

        self.assertEquals(self.mcrb.member_company.balance, balance - self.mcrb.get_quote_price())
        self.assertEquals(memberbillinghistory_set.count(), 1)
        
#        self.assertEquals(True,False)