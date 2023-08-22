from django.urls import path
from . import views
from .views import error_404_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Myapp.as_view(), name='myapp'),
    path('monitoring_stations/', views.monitoring_stations_view, name='monitoring_stations'),
    path('monitoring_stations/add/', views.add_monitoring_station, name='add_monitoring_station'),
    path('monitoring_stations/<int:pk>/edit/', views.edit_monitoring_station, name='edit_monitoring_station'),
    path('monitoring_stations/<int:pk>/delete/', views.delete_monitoring_station, name='delete_monitoring_station'),
    path('equipment_type/', views.equipment_type_view, name='equipment_type'),
]

handler404 = 'myapp.views.error_404_view'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)