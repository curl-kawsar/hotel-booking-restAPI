from django.contrib import admin
from .models import Destination, Room, Hotel, TopDestination, RecommendedPlace, Contact

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'number_of_beds', 'is_ac', 'accommodates')

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'destination', 'total_adults', 'total_childrens', 'availability', 'price_per_night')

@admin.register(TopDestination)
class TopDestinationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body', 'images')

@admin.register(RecommendedPlace)
class RecommendedPlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'location', 'reviews', 'description', 'price')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'number', 'message')