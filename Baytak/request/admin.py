from django.contrib import admin
from .models import  Request
# Register your models here.


admin.site.register(Request)


from services.models import Service

class Request(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    note = models.TextField()
    date = models.DateTimeField()
    status = models.CharField(length = 1024, default = "pending")
    initial_price = models.PositiveIntegerField()

class RequestComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    comment = models.TextField()