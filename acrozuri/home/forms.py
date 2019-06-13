from django import forms
from django.utils.translation import ugettext_lazy as _
from acrozuri.home.models import Member, News


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name',
                  'last_name',
                  'b_date',
                  'address',
                  'post_code',
                  'city',
                  'country',
                  'phone',
                  'email',
                  'note',
                  ]
        labels = {
            'b_date': _('Birthday')
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Max'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Munster'}),
            'b_date': forms.DateInput(attrs={'placeholder': '12/12/1990'}),
        }


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ['name',
                  'email',
                  'subject',
                  'message',
                  ]
