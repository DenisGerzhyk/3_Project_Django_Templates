from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str(self):
        return f'{self.name} + {self.email}'
