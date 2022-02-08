from django.urls import path
from.import views

urlpatterns = [
    path('event', views.event, name='event'),
    path('event/<int:pk>', views.event_details, name='event_details'),
]
