from django.contrib import admin

from .models import MenuItem,  MenuItemAdmin
from .models import MenuSubItem, MenuSubItemAdmin
from .models import MenuItemType, MenuItemTypeAdmin

admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(MenuSubItem, MenuSubItemAdmin)
admin.site.register(MenuItemType, MenuItemTypeAdmin)