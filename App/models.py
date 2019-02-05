from django.db import models


class RFModel(models.Model):
    name = models.CharField(max_length=250)
    model = models.BinaryField(null=True)

    def __str__(self):
        return f'{self.name}'
