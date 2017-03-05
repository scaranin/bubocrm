from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext as _

#=================================================================================
class CustomerType(models.Model):
    class Meta:
        db_table = "tbl_customertype"
        verbose_name = _('��� �������')
        verbose_name_plural = _('01 ���� ��������')
    customertype_id = models.AutoField(primary_key=True)
    customertype_name = models.CharField("������������", max_length=256)
    def __str__(self):
        return self.customertype_name
#=================================================================================

#=================================================================================
class FieldType(models.Model):
    class Meta:
        db_table = "tbl_fieldtype"
        verbose_name = _('��� ����')
        verbose_name_plural = _('02 ���� �����')
    fieldtype_id = models.AutoField(primary_key=True)
    fieldtype_name = models.CharField("������������", max_length=256)
    fieldtype_descr = models.CharField("��������", max_length=256, blank=True)
    def __str__(self):
        return self.fieldtype_descr

class FieldTypeAdmin(admin.ModelAdmin):
    list_display = ('fieldtype_name', 'fieldtype_descr')
#=================================================================================

#=================================================================================
class Owner(models.Model):
    class Meta:
        db_table = "tbl_owner"
        verbose_name = _('����������')
        verbose_name_plural = _('03 �����������')

    owner_type = models.ForeignKey(CustomerType, verbose_name = '��� �������')

    owner_id = models.AutoField(primary_key=True)
    owner_name = models.CharField("������������", max_length=256)
    owner_address_jur = models.CharField("����������� �����", max_length=256)
    owner_address_post = models.CharField("�������� �����", max_length=256)
    owner_ogrn = models.CharField("����", max_length=13)
    owner_inn = models.CharField("���", max_length=12)
    owner_kpp = models.CharField("���", max_length=9)
    owner_account = models.CharField("��������� ����", max_length=20)

    def __str__(self):
        return self.owner_name
#=================================================================================

#=================================================================================
class CustomerShablon(models.Model):
    class Meta:
        db_table = "tbl_customershablon"
        verbose_name = _('������ �������')
        verbose_name_plural = _('04 ������� ��������')

    owner = models.ForeignKey(Owner, verbose_name = '����������')

    CustomerShablon_id = models.AutoField(primary_key=True)
    CustomerShablon_Name = models.CharField("������������", max_length=256)

    def Attributes(self):
        return CustomerAttribute.objects.filter(customershablon=self).order_by('CustomerShablon_id')
    
    def __str__(self):
        return self.CustomerShablon_Name
#=================================================================================

#=================================================================================
class CustomerAttribute(models.Model):
    class Meta:
        db_table = "tbl_customerattribute"
        verbose_name = _('�������� �������')
        verbose_name_plural = _('05 �������� ��������')
    
    customershablon = models.ForeignKey(CustomerShablon, verbose_name='������ �������',)
    attr_type = models.ForeignKey(FieldType, verbose_name = '��� ����')

    attr_id = models.AutoField(primary_key=True)
    attr_name = models.CharField("������������", max_length=256)
    attr_desc = models.CharField("��������", max_length=256, blank=True)
    attr_mask = models.CharField("�����", max_length=50, blank=True)
    
    flag_yes = 1
    flag_no = 2
    attr_nullable_choices = (
        (flag_yes, '��'),
        (flag_no, '���'),
    )
    attr_nullable = models.IntegerField("�������������� ����������", 
                                        choices=attr_nullable_choices, 
                                        null=False,
                                        default=flag_no)
    status = models.IntegerField("������", null=False)
    
    def __str__(self):
        return self.attr_name

class CustomerAttributeAdmin(admin.ModelAdmin):
    list_display = ('customershablon', 'attr_type', 'attr_name', 'attr_desc')
    list_filter = ('customershablon',)
#=================================================================================
    
#=================================================================================
class Customer(models.Model):
    class Meta:
        db_table = "tbl_customer"
        verbose_name = _('������')
        verbose_name_plural = _('06 �������')
    
    customershablon = models.ForeignKey(CustomerShablon, verbose_name = '������ �������', related_name = 'customers')
    customer_type = models.ForeignKey(CustomerType, verbose_name = '��� �������')
    
    customer_id  = models.AutoField('���', primary_key=True)
    customer_name = models.CharField('���', max_length=256)
    ext_attr_value = models.CharField('������', max_length=256)
    status = models.IntegerField('������', null=False)
    create_date = models.DateField('���� ���������', auto_now=True)
    
    def __str__(self):
        return self.customer_name

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customershablon', 'customer_type', 'customer_name', 'ext_attr_value', 'status', 'create_date')
    list_filter = ('customershablon', 'customer_type',)
#=================================================================================

#=================================================================================
class CustomerAttrVal(models.Model):
    class Meta:
        db_table = "tbl_customerattrval"
        verbose_name = _('�������� ��������� �������')
        verbose_name_plural = _('07 �������� ��������� ��������')
    customer = models.ForeignKey(Customer, verbose_name = '������', related_name = 'customerattrvals')
    cli_attr = models.ForeignKey(CustomerAttribute, verbose_name = '�������� �������')

    ext_attr = models.AutoField(primary_key=True)
    cli_attr_value = models.CharField('��������', max_length=256)

class CustomerAttrValAdmin(admin.ModelAdmin):
    list_display = ('customer', 'cli_attr', 'cli_attr_value')
    list_filter = ('customer',)
#=================================================================================

"""
https://hh.kz/vacancy/8059458
https://hh.kz/vacancy/15107429
CREATE TABLE BAS.tbl_cont_folder
  (
    folder_id NUMBER NOT NULL ,
    customer_id NUMBER NOT NULL
  ) ;

CREATE TABLE BAS.tbl_contract
  (
    cont_id     NUMBER NOT NULL ,
    prod_id     NUMBER NOT NULL ,
    user_id     NUMBER NOT NULL ,
    crdatetime  DATE ,
    cont_status NUMBER ,
    cont_sum    NUMBER ,
    folder_id   NUMBER NOT NULL ,
    product_id  NUMBER NOT NULL
  ) ;

CREATE TABLE BAS.tbl_meashure
  (
    meash_id  NUMBER NOT NULL ,
    meashname VARCHAR2 (100) ,
    owner_id  NUMBER NOT NULL
  ) ;

CREATE TABLE tbl_product
  (
    product_id   NUMBER NOT NULL ,
    owner_id     NUMBER NOT NULL ,
    product_name VARCHAR2 (100) ,
    product_cost NUMBER ,
    meash_id     NUMBER NOT NULL ,
    prodtype_id  NUMBER NOT NULL
  ) ;

CREATE TABLE BAS.tbl_producttype
  (
    prodtype_id  NUMBER NOT NULL ,
    prodtypename VARCHAR2 (256) ,
    owner_id     NUMBER NOT NULL
  ) ;

CREATE TABLE BAS.tbl_user
  (
    user_id    NUMBER NOT NULL ,
    username   VARCHAR2 (20) ,
    userfio    VARCHAR2 (100) ,
    userstatus NUMBER ,
    owner_id   NUMBER NOT NULL
  ) ;
"""