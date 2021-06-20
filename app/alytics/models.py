from django.db import models

# Приводит к зацикливанию с таском
from alytics.tasks import create_graphic


class GraphFunc(models.Model):
    title = models.CharField(max_length=100)
    interval = models.IntegerField()
    dt = models.IntegerField()
    create_datetime = models.DateTimeField(auto_now=True)
    graphic = models.ImageField(null=True, blank=True, editable=False, upload_to='images/')
    func_exception = models.TextField(null=True, blank=True, editable=False)

    def __str__(self) -> str:
        return str(self.title)

    # def save(self, *args, **kwargs):
    #     do_something()
    #     super().save(*args, **kwargs)  # Call the "real" save() method.
    #     do_something_else()


def grahp_func_save(sender, instance, signal, *args, **kwargs):
    '''create image'''
    create_graphic.delay(instance.pk)


# https://code.tutsplus.com/ru/tutorials/using-celery-with-django-for-background-task-processing--cms-28732
models.signals.post_save.connect(grahp_func_save, sender=GraphFunc)
