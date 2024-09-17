from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
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

@api_view(['GET'])
def check_availability(request):
    destination_id = request.query_params.get('destination')
    check_in_date = request.query_params.get('check_in_date')
    check_out_date = request.query_params.get('check_out_date')
    total_adults = request.query_params.get('total_adults')
    total_childrens = request.query_params.get('total_childrens')

    # Filter hotels based on the criteria
    hotels = Hotel.objects.filter(
        destination_id=destination_id,
        availability=True,
        total_adults__gte=total_adults,
        total_childrens__gte=total_childrens
    )

    serializer = HotelSerializer(hotels, many=True)
    return Response(serializer.data)
