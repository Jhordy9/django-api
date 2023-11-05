from api.forms.member import MemberForm
from api.models.member import Member
from django.core import serializers
from django.forms.models import model_to_dict


class MemberService:
    @staticmethod
    def member_list():
        members = Member.objects.all()
        members_json = serializers.serialize('json', members)
        return members_json

    @staticmethod
    def member_by_pk(pk: int):
        member = Member.objects.get(pk=pk)
        return model_to_dict(member)

    @staticmethod
    def add_member(data):
        form = MemberForm(data)
        if form.is_valid():
            return form.save()
        else:
            raise ValueError("Invalid member data")
