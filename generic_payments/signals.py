from django import dispatch

pizza_done = dispatch.Signal(providing_args=["toppings", "size"])

class PaymentSignal(dispatch.Signal):
    """Base class for all payment signals"""
    providing_args = []

    def __init__(self):
        super(PaymentSignal, self).__init__(self.providing_args)
#
#class OperationCompleted(PaymentSignal):
#    """Base class for all payment signals"""
#    providing_args = ["operation", "receiver"]
#
#_operation_completed_signal = OperationCompleted()
#
#class PaymentSignalDispatcher(object):
#
#    def operation_completed(self, operation, receiver):
#        _operation_completed_signal.send(
#            sender=self,
#            operation=operation,
#            receiver=receiver
#        )
#
#payment_signal_dispatcher = PaymentSignalDispatcher()