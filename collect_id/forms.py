from django.forms import ModelForm, Form
from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Info
class InfoForm(ModelForm):
    class Meta:
        model = Info
        fields = '__all__'
        labels = {
            'name': _('姓名'),
            'stu_id': _('学号'),
            'soj_id': _('SOJ ID'),
            'cf_id': _('Codeforces ID'),
            'bc_id': _('BestCoder ID'),
        }

class DeleteForm(Form):
    stu_id = forms.CharField(label='学号')