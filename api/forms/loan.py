from django import forms
from api.models.loan import Loan


class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ['loan_date', 'book', 'member']

    def save(self, commit=True):
        return super().save(commit=commit)
