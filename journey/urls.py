from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register(r'destinations', views.DestinationViewSet)
router.register(r'rooms', views.RoomViewSet)
router.register(r'hotels', views.HotelViewSet)
router.register(r'top-destinations', views.TopDestinationViewSet)
router.register(r'recommended-places', views.RecommendedPlaceViewSet)
router.register(r'contacts', views.ContactViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/check-availability/', views.check_availability, name='check-availability'),
]
