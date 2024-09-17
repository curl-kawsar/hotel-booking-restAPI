from rest_framework import viewsets
from .models import Destination, Room, Hotel, TopDestination, RecommendedPlace, Contact
from .serializers import DestinationSerializer, RoomSerializer, HotelSerializer, TopDestinationSerializer, RecommendedPlaceSerializer, ContactSerializer

class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class TopDestinationViewSet(viewsets.ModelViewSet):
    queryset = TopDestination.objects.all()
    serializer_class = TopDestinationSerializer

class RecommendedPlaceViewSet(viewsets.ModelViewSet):
    queryset = RecommendedPlace.objects.all()
    serializer_class = RecommendedPlaceSerializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer