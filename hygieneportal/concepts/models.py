from django.db import models
from django.db.models import fields, CharField, QuerySet
import base64
# Create your models here.


class Contact(models.Model):
    name = CharField(max_length=100)
    email = fields.EmailField()

    def __str__(self):
        return "{} ({})".format(self.name, self.email)

    def mail_url(self):
        mailto = "mailto:{}<{}>".format(self.name, self.email)
        encoded_mail = base64.b64encode(mailto.encode()).decode()
        return "javascript:window.location.href=atob('{}')".format(encoded_mail)


class Concept(models.Model):
    name = CharField(max_length=50, default="Hygienekonzept")
    pdf = models.FileField(upload_to='concepts/')

    def __str__(self):
        related_clubs: QuerySet = Club.objects.filter(concepts=self)
        if related_clubs.count() > 0:
            return "{}: {}".format(related_clubs.first(), self.name)
        else:
            return "{}".format(self.name)


class Club(models.Model):
    name = CharField(max_length=100)
    contacts = models.ManyToManyField(Contact)
    concepts = models.ManyToManyField(Concept)
    access_count = fields.IntegerField(default=0)

    def __str__(self):
        return self.name

    def access(self):
        self.access_count += 1
        self.save()

    class Meta:
        ordering = ['-access_count']
