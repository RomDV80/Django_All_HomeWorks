from django.urls import path
from .views import SensorView, SensorDetailView, MeasurementView

urlpatterns = [
    path('sensors/', SensorView.as_view(), name='sensor-list'),
    path('sensors/<int:pk>/', SensorDetailView.as_view(), name='sensor-detail'),
    path('measurements/', MeasurementView.as_view(), name='measurement-create'),
]
