from django.conf.urls.defaults import *

urlpatterns = patterns('payments.views',
    url(r'^$', 'ipn', name="paypal-ipn"),
)