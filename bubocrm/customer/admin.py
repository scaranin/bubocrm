from django.contrib import admin

from .models import Owner, CustomerType, CustomerAttribute, CustomerAttributeAdmin, Customer, CustomerAdmin, CustomerAttrVal, CustomerAttrValAdmin, CustomerShablon, FieldType, FieldTypeAdmin

admin.site.register(CustomerType)
admin.site.register(Owner)
admin.site.register(CustomerShablon)
admin.site.register(CustomerAttribute, CustomerAttributeAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(CustomerAttrVal, CustomerAttrValAdmin)
admin.site.register(FieldType, FieldTypeAdmin)

