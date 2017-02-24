from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from django_tables2   import RequestConfig
from django.contrib.auth.models import AnonymousUser
from .tables  import CustomerTable
from .models import Owner, CustomerType, CustomerAttribute, Customer, CustomerAttrVal

def index(request):
    if hasattr(request, 'user'):
        user = request.user
    else:
        user = AnonymousUser()
    if request.method == 'POST':
        CusId = request.POST.get('CusId', False)
        CusName = request.POST.get('CusName', False)
        CusDopData = request.POST.get('CusDopData', False)
        CustomerList = Customer.objects.filter(customer_name__icontains=CusName, ext_attr_value__icontains=CusDopData)
        CustomerListCount = Customer.objects.filter(customer_name__icontains=CusName, ext_attr_value__icontains=CusDopData).count()
        AttributeList = CustomerAttribute.objects.all()
        AttributeValueList = CustomerAttrVal.objects.all()
    else:
        CustomerList = None
        CustomerListCount = 0
        AttributeList = None
        AttributeValueList = None
    return render(request, 'customer/index.html', {'user':user, 'CustomerListCount': CustomerListCount, 'CustomerList': CustomerList, 'AttributeList' : AttributeList, 'AttributeValueList' : AttributeValueList,})


