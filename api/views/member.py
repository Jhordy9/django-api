from django.http import Http404, HttpResponse, HttpResponseBadRequest, JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
import json

from api.models.member import Member
from api.services.member import MemberService


@require_http_methods(["GET"])
def member_list(_):
    members = MemberService.member_list()
    return HttpResponse(members, content_type="application/json")


@require_http_methods(["GET"])
def member_by_pk(_, pk: int):
    try:
        member = MemberService.member_by_pk(pk)
        return JsonResponse(member, content_type="application/json")
    except Member.DoesNotExist:
        raise Http404("Member does not exist")


@require_http_methods(["POST"])
@csrf_exempt
def add_member(request):
    try:
        member_data = json.loads(request.body.decode('utf-8'))
        member = MemberService.add_member(member_data)
        return HttpResponse(member, status=201)
    except:
        return HttpResponseBadRequest('Invalid data provided for the member.')
