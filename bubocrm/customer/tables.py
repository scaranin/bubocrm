import django_tables2 as tables
from customer.models import Customer

class CustomerTable(tables.Table):
    class Meta:
        model = Customer
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}
