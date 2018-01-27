from django.db import models


class Measurement(models.Model):
    station = models.IntegerField()
    #  ...
    # TODO: add fields

    class Meta:
        # we can't make use of the database, managed = False makes sure it doesn't save the model
        managed = False
