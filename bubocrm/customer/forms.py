from django import forms
from .models import Post

class CDBForm(forms.Form):
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
        forms.Form.__init__(self, *args, **kwargs)