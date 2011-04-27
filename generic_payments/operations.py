
# should be interface?
class Operation(object):
    type = 'none'

    def __init__(self, **kwargs):
        super(Operation, self).__init__()

    def get_cost(self):
        pass

    def post_process(self):
        pass

class CreditOperation(Operation):
    type = 'credit'
    
    def __init__(self, **kwargs):
        super(CreditOperation, self).__init__(**kwargs)
    
    def __rsub__(self, other):
        return other + self.get_cost()

class ChargeOperation(Operation):
    type = 'charge'
    
    def __init__(self, **kwargs):
        super(ChargeOperation, self).__init__(**kwargs)
    
    def __radd__(self, other):
        return other - self.get_cost()