from django import forms
from .models import CustomerShablon, CustomerAttribute
from .files import log

class CustomerShablonForm(forms.Form):
    def __init__(self, customershablon=None, tag=None, *args, **kwargs):
        #for cus_id in CustomerShablon.objects.all():
         #   log(str(cus_id.CustomerShablon_id))
          #  log(str(cus_id.CustomerShablon_Name))
        #log(str(CustomerShablon.objects.get(CustomerShablon_id='1')))
        self.customershablon = CustomerShablon.objects.get(CustomerShablon_id='2')
        Attributes = CustomerAttribute.objects.filter(customershablon=self.customershablon)
        #log(str(self.customershablon))
        for attribute in Attributes:
            self.base_fields[attribute.attr_id] = forms.CharField(label=attribute.attr_name, required=True)
        forms.Form.__init__(self, *args, **kwargs)

'''
from django import forms
from .models import CustomerAttribute, CustomerShablon, FieldType

class CustomerForm(forms.Form):
    def __init__(self, template=None, tag=None, *args, **kwargs):
        if template:
            self.template = template
        elif tag:
            self.template = Template.objects.get(tag=tag)
        fields = self.template.fields()
        for field in fields:
            if field.type == "B":
                self.base_fields[field.tag] = forms.BooleanField(label=field.title, required=field.required)
            elif field.type == "T":
                self.base_fields[field.tag] = forms.CharField(label=field.title, required=field.required)
            elif field.type == "C":
                choices = []
                for parameter in field.parameters():
                    if parameter.tag == "choice":
                        choices.append((parameter.value, parameter.value))
                self.base_fields[field.tag] = forms.ChoiceField(choices=choices, label=field.title, required=field.required)
            elif field.type == "E":
                self.base_fields[field.tag] = forms.EmailField(label=field.title, required=field.required)
            elif field.type == "U":
                self.base_fields[field.tag] = forms.URLField(label=field.title, required=field.required)
        forms.Form.__init__(self, *args, **kwargs)'''