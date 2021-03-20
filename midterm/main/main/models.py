from django.db import models


class BookJournalBase(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField()
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField()

    class Meta:
        abstract = True


class Book(BookJournalBase):
    num_pages = models.IntegerField
    genre = models.CharField(max_length=50)


class Journal(BookJournalBase):
    JOURNAL_TYPE = (
        ('BULLET', 'bullet'),
        ('FOOD', 'food'),
        ('TRAVEL', 'travel'),
        ('SPORT', 'sport'),
    )
    type = models.CharField(max_length=150)
    publisher = models.CharField(max_length=150)
