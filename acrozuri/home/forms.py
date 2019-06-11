from django import forms
from acrozuri.home.models import Member, News


class RegisterForm(forms.ModelForm):
    action = forms.CharField(max_length=60, widget=forms.HiddenInput())

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


class NewsForm(forms.ModelForm):
    action = forms.CharField(max_length=60, widget=forms.HiddenInput())

    class Meta:
        model = News
        fields = ['name',
                  'email',
                  'subject',
                  'message'
                  ]
