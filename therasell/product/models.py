
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

CONDITION = (
    ('New with Tags','New with Tags'),
    ('New without tags','New without tags'),
    ('Excellent','Excellent'),
    ('Good','Good'),
    ('Good','Fair'),
    ('Good','Poor'),
)

CATEGORIES = (
('Geriatric','Geriatric'),
('Sports injury','Sports injury'),
('Sensory','Sensory'),
('Gross Motor','Gross Motor'),
('Fine motor','Fine motor'),
('Wheel chairs','Wheel chairs'),
('Mobility (walkers, Canes, crawlers, ramps)','Mobility (walkers, Canes, crawlers, ramps)'),
('Walkers and Fall Safety','Walkers and Fall Safety'),
('Splints and braces','Splints and braces'),
('Activities of daily living','Activities of daily living'),
('Durable medical equipment','Durable medical equipment'),
('Rehabilitation and Physical Therapy','Rehabilitation and Physical Therapy'),
('Visual Motor/Visual Perceptual','Visual Motor/Visual Perceptual'),
('Assessments','Assessments')
)


class Product(models.Model):

    ID = models.IntegerField(primary_key = True)
    Title = models.CharField(max_length=50)
    Description = models.TextField()
    Category = models.CharField(choices=CATEGORIES, max_length=100)
    Quantity = models.IntegerField(validators=[MinValueValidator(0)],default=1)
    Size = models.CharField(max_length=10,blank=True,null=True)
    Image = models.ImageField(upload_to = 'pic_folder/')
    Brand = models.CharField(max_length=50,blank=True,null=True)
    Color = models.CharField(max_length=20,blank=True,null=True)
    Condition = models.CharField(choices=CONDITION, max_length=25)    
    Seller = models.TextField()
    Original_Price = models.CharField(max_length=10)
    Listing_Price = models.CharField(max_length=10)

    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

