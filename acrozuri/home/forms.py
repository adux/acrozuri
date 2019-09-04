from datetime import datetime
from django import forms
from django.utils.translation import ugettext_lazy as _
from acrozuri.home.models import Member, News

min_age = 10
this_year = datetime.now().year


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
            'first_name': forms.TextInput(attrs={'placeholder': 'Example: Max'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Example: Muster'}),
            'b_date': forms.SelectDateWidget(empty_label={"Choose Year", "Choose Month", "Choose Day"},
                                             years=range(this_year - (min_age + 80), this_year - min_age),
                                             ),
            'phone': forms.TextInput(attrs={'placeholder': '+4179123456'}),
        }


class NewsForm(forms.ModelForm):
    action = forms.CharField(max_length=60, widget=forms.HiddenInput())

    class Meta:
        model = News
        fields = ['name',
                  'email',
                  'subject',
                  'message',
                  ]
