
from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.
class Product(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product_id = models.IntegerField(primary_key = True)
    product_description = models.TextField()
    title = models.CharField(max_length=200)
    Image = models.TextField(null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    category = models.TextField()
    price = models.IntegerField()


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title