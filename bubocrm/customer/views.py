from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from django_tables2   import RequestConfig
from django.contrib.auth.models import AnonymousUser
from .tables  import CustomerTable
from .models import Owner, CustomerType, CustomerAttribute, Customer, CustomerShablon, CustomerAttrVal
from menu.models import MenuItem, MenuSubItem
from .files import log

def index(request):
    # Определение пользователя
    if hasattr(request, 'user'):
        user = request.user
    else:
        user = AnonymousUser()
		
    MenuList = MenuItem.objects.filter(ParentMenu__iexact=None).order_by('ItemOrder')
    SubMenuList = MenuItem.objects.order_by('ItemOrder')

    # Получение данных по клиентам
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
    
    # Шаблоны клиентов
    CustomerShablonList = CustomerShablon.objects.all()
    CustomerShablonAttr = {}
    for CustomerShablonItem in CustomerShablonList:
        CustomerShablonAttr = {CustomerShablonItem.CustomerShablon_id: CustomerAttributeList for CustomerAttributeList in CustomerAttribute.objects.filter(customershablon=CustomerShablonItem)}
    return render(request, 'customer/main/customer.html', {'user':user,
														   'CustomerListCount': CustomerListCount, 
														   'CustomerList': CustomerList, 
														   'AttributeList' : AttributeList, 
														   'AttributeValueList' : AttributeValueList, 
														   'CustomerShablonList': CustomerShablonList,
														   'CustomerShablonAttr': CustomerShablonAttr,
														   'MenuList': MenuList,
														   'SubMenuList' : SubMenuList,})

def data_customer(request, customer_id = None):
    # Получение данных по клиенту
    CustomerItem = Customer.objects.get(customer_id=customer_id)
    CustomerAttrDataList = CustomerAttrVal.objects.filter(customer = CustomerItem)
    return render(request, 'customer/main/customer/customer_data.html', {
                                                   'CustomerItem': CustomerItem,
                                                   'CustomerAttrDataList': CustomerAttrDataList})
