
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, IntegerField, TextField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User


class restaurant(models.Model):
    name = CharField(null=False,max_length=120)
    kitchen_type = CharField(max_length=120)
    img_path = CharField(null=False,max_length=255)
    street = CharField(max_length=120)
    local_number = CharField(max_length=120)
    city = CharField(max_length=120)
    pass_code = IntegerField()
    owner = ForeignKey(User, on_delete=CASCADE, null=False, related_name="owns")



