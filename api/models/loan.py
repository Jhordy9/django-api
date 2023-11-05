from django.db import models
from django.utils import timezone

from api.models.book import Book
from api.models.member import Member


class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    loan_date = models.DateField()
    return_date = models.DateField(null=True)

    def is_returned(self) -> bool:
        return self.return_date is not None and self.return_date <= timezone.localdate()

    def is_late(self) -> bool:
        return self.loan_date > timezone.localdate() + timezone.timedelta(days=3)
