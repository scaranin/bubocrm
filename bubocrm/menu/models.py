from django.db import models
from django.contrib import admin

class MenuItemType(models.Model):
    ItemTypeId = models.AutoField(primary_key=True)
    ItemTypeName = models.CharField('Тип элемента меню', max_length=50)
    ItemTypeShowName = models.CharField('Отображаемое имя', max_length=50, default='')
    def __str__(self):
        return self.ItemTypeName
class MenuItemTypeAdmin(admin.ModelAdmin):
    list_display = ('ItemTypeName', )

class MenuItem(models.Model):
    ItemId = models.AutoField(primary_key=True)
    ItemName = models.CharField('Наименование элемента меню', max_length=50)
    ItemShowName = models.CharField('Отображаемое имя', max_length=50, default='')
    ItemClick = models.CharField('Событие по клику', max_length=100)
    ItemIsActive = models.IntegerField('Признак активности', default=0)
    ItemOrder = models.IntegerField('Порядок группировки', default=0)
    ItemType = models.ForeignKey(MenuItemType)
    ParentMenu = models.ForeignKey('self', blank=True, null=True, related_name='ChildMenu')
    def __str__(self):
        return self.ItemName
    
    def GetChildItems(self):
        return MenuItem.objects.filter(ParentMenu__iexact=self.ItemId).order_by('ItemOrder')

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('ItemShowName', 'ParentMenu', 'ItemName', 'ItemIsActive', 'ItemOrder', 'ItemType')

class MenuSubItem(models.Model):
    SubItemId = models.AutoField(primary_key=True)
    ParentMenu = models.ForeignKey(MenuItem)
    SubItemName = models.CharField('Наименование подэлемента меню', max_length=50)
    SubItemClick = models.CharField('Событие по клику', max_length=100)
    SubItemOrder = models.IntegerField('Порядок группировки', default=0)
    def __str__(self):
        return self.SubItemName

class MenuSubItemAdmin(admin.ModelAdmin):
    list_display = ('ParentMenu', 'SubItemName', 'SubItemOrder')