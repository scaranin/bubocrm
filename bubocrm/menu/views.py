from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import MenuItem, MenuSubItem

def index(request):
    MenuList = MenuItem.objects.filter(ParentMenu__iexact=None).order_by('ItemOrder')
    SubMenuList = MenuItem.objects.order_by('ItemOrder')
    template = loader.get_template('main/index.html')
    context = RequestContext(request, {
        'MenuList': MenuList,
        'SubMenuList' : SubMenuList,
    })
    return HttpResponse(template.render(context))