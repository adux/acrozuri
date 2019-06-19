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
            'first_name': forms.TextInput(attrs={'placeholder': 'Example: Max'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Example: Munster'}),
            'b_date': forms.SelectDateWidget(attrs={'placeholder': '1945-10-10'},
                                             empty_label={"Choose Year", "Choose Month", "Choose Day"}
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
