from typing_extensions import Required
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import IntegerField, TextField
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User


class restaurant(models.Model):
    name = TextField(Required=True)
    kitchen_type = TextField()
    img_path = TextField(Required=True)
    street = TextField()
    local_number = TextField()
    city = TextField
    pass_code = IntegerField(max_length=5)
    owner_id = ForeignKey(User, on_delete=CASCADE, Required=True, related_name="owns")



