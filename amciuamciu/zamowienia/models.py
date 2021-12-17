from typing import Callable
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, TextField, DecimalField, EmailField
from django.db.models.fields.related import ForeignKey, ForeignObject

from restaurant.models import restaurant as rest
