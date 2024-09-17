from rest_framework import serializers
from .models import Destination, Room, Hotel, TopDestination, RecommendedPlace, Contact

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'

class TopDestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopDestination
        fields = '__all__'

class RecommendedPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendedPlace
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class AvailabilityCheckSerializer(serializers.Serializer):
    destination = serializers.IntegerField()
    total_adults = serializers.IntegerField()
    total_childrens = serializers.IntegerField()