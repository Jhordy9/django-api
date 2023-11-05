from django.http import Http404, HttpResponse, HttpResponseBadRequest, JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json

from api.models.loan import Loan
from api.services.loan import LoanService


@require_http_methods(["GET"])
def loan_list(request):
    not_returned = request.GET.get('not_returned')
    loans = LoanService.loan_list(not_returned)
    return HttpResponse(loans, content_type="application/json")


@require_http_methods(["GET"])
def loan_by_pk(_, pk: int):
    try:
        loan = LoanService.loan_by_pk(pk)
        return JsonResponse(loan, content_type="application/json")
    except Loan.DoesNotExist:
        raise Http404("Loan does not exist")


@require_http_methods(["POST"])
@csrf_exempt
def add_loan(request):
    try:
        loan_data = json.loads(request.body.decode('utf-8'))
        loan = LoanService.add_loan(loan_data)
        return JsonResponse({'loan_id': loan.id}, status=201)
    except ValueError as e:
        return HttpResponseBadRequest(str(e))
    except Exception as e:
        return HttpResponseBadRequest(f'An error occurred: {str(e)}')
