from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    
class Room(models.Model):
    type = models.CharField(max_length=100)
    number_of_beds = models.IntegerField(default=1)
    is_ac = models.BooleanField(default=False)
    accommodates = models.IntegerField(default=1)

    def __str__(self):
        return self.type
    
TOTAL_ADULTS = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
]

TOTAL_CHILDRENS = [
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
]


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    rooms = models.ManyToManyField(Room)
    total_adults = models.CharField(max_length=2, choices=TOTAL_ADULTS)
    total_childrens = models.CharField(max_length=2, choices=TOTAL_CHILDRENS)
    availability = models.BooleanField(default=True)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    
class TopDestination(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    images = models.TextField()

    def __str__(self):
        return self.title

REVIEW_CHOICES = [
    ('⭐', '⭐'),
    ('⭐⭐', '⭐⭐'),
    ('⭐⭐⭐', '⭐⭐⭐'),
    ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
]

class RecommendedPlace(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    reviews = models.CharField(max_length=10, choices=REVIEW_CHOICES)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
    
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=15)
    message = models.TextField()
    
    
    def __str__(self):
        return self.name