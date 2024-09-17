from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from .models import Destination, Room, Hotel, TopDestination, RecommendedPlace, Contact
from .serializers import DestinationSerializer, RoomSerializer, HotelSerializer, TopDestinationSerializer, RecommendedPlaceSerializer, ContactSerializer, AvailabilityCheckSerializer

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

@api_view(['GET', 'PUT'])
def check_availability(request):
    if request.method == 'GET':
        return render(request, 'check_availability.html')
    elif request.method == 'PUT':
        serializer = AvailabilityCheckSerializer(data=request.data)
        if serializer.is_valid():
            destination_id = serializer.validated_data['destination']
            total_adults = serializer.validated_data['total_adults']
            total_childrens = serializer.validated_data['total_childrens']

            hotels = Hotel.objects.filter(
                destination_id=destination_id,
                availability=True,
                total_adults__gte=total_adults,
                total_childrens__gte=total_childrens
            )

            if hotels.exists():
                hotel_names = [hotel.name for hotel in hotels]
                return Response({"message": "Yes, Available", "hotels": hotel_names})
            else:
                return Response({"message": "No, Not Available"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)