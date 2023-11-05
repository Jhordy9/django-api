from django import forms
from api.models.member import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'email']
