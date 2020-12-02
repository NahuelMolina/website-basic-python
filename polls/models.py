from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField(null=True)
    email = models.CharField(max_length=190)


class Pets(models.Model):
    Owner_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='%(class)s_Owner_id', null=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField(null=True)


class Devices(models.Model):
    model = models.CharField(max_length=100)
    operating_system = models.CharField(max_length=100)
    api_token = models.CharField(max_length=191)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='%(class)s_user_id', null=True)



