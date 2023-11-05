from django.core import serializers
from api.forms.loan import LoanForm
from api.models.loan import Loan
from django.forms.models import model_to_dict


class LoanService:
    @staticmethod
    def add_loan(data):
        form = LoanForm(data)
        if form.is_valid():
            loan = form.save(commit=False)
            loan.save()
            return loan
        else:
            print(form.errors)
            raise ValueError(f"Form data is not valid: {form.errors}")

    def loan_list(not_returned: bool):
        loans = Loan.objects.order_by('loan_date')

        if not_returned:
            loans = loans.filter(return_date__isnull=True)

        loans_json = serializers.serialize('json', loans)
        return loans_json

    def loan_by_pk(pk: int):
        loan = Loan.objects.get(pk=pk)
        return model_to_dict(loan)
