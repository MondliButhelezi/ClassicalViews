from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.MyappView.as_view(), name='myapp'),
    path('monitoring_stations/', views.MonitoringStationsView.as_view(), name='monitoring_stations'),
    path('monitoring_stations/add/', views.AddMonitoringStationView.as_view(), name='add_monitoring_station'),
    path('monitoring_stations/<int:pk>/edit/', views.EditMonitoringStationView.as_view(), name='edit_monitoring_station'),
    path('monitoring_stations/<int:pk>/delete/', views.DeleteMonitoringStationView.as_view(), name='delete_monitoring_station'),

    path('equipment_type/', views.EquipmentTypeView.as_view(), name='equipment_type'),
    path('equipment_type/add/', views.AddEquipmentTypeView.as_view(), name='add_equipment_type'),
    path('equipment_type/<int:pk>/edit/', views.EditEquipmentTypeView.as_view(), name='edit_equipment_type'),
    path('equipment_type/<int:pk>/delete/', views.DeleteEquipmentTypeView.as_view(), name='delete_equipment_type'),

]

handler404 = 'myapp.views.error_404_view'

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
