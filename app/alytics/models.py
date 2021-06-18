from django.db import models

class GraphFunc(models.Model):
    title = models.CharField(max_length=100)
    graphic = models.ImageField()
    func_exception = models.TextField(null=True, blank=True, editable=False)
    interval = models.IntegerField()
    dt = models.IntegerField()
    create_datetime = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.title)