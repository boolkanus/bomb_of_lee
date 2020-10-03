from django.db import models
from django.contrib.auth.models import User

# 폭탄을 돌리는 주체
class MoveCmd(models.Model):
    user = models.CharField
    direction = models.CharField
