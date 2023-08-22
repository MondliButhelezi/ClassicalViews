from django.shortcuts import render, get_object_or_404, redirect
from .models import MonitoringStation, EquipmentType
from django import forms
from django.views import View
from django.http import HttpResponse


# Create your views here.

class Myapp(View):
    def get(self, request):
        return render(request, 'myapp.html')



def monitoring_stations_view(request):
    monitoring_stations = MonitoringStation.objects.all()
    return render(request, 'stations/monitoring_stations.html', {'object_list': monitoring_stations})


def add_monitoring_station(request):
    if request.method == 'POST':
        form = MonitoringStationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('monitoring_stations')
    else:
        form = MonitoringStationForm()
    return render(request, 'stations/add_monitoring_station.html', {'form': form})


def edit_monitoring_station(request, pk):
    station = get_object_or_404(MonitoringStation, pk=pk)
    if request.method == 'POST':
        form = MonitoringStationForm(request.POST, instance=station)
        if form.is_valid():
            form.save()
            return redirect('monitoring_stations')
    else:
        form = MonitoringStationForm(instance=station)
    return render(request, 'stations/edit_monitoring_station.html', {'form': form})


def delete_monitoring_station(request, pk):
    station = get_object_or_404(MonitoringStation, pk=pk)
    if request.method == 'POST':
        station.delete()
        return redirect('monitoring_stations')
    return render(request, 'stations/delete_monitoring_station.html', {'station': station})


# forms
class MonitoringStationForm(forms.ModelForm):
    class Meta:
        model = MonitoringStation
        fields = '__all__'


def equipment_type_view(request):
    equipment_type = EquipmentType.objects.all()
    return render(request, 'equipment/equipment_type.html',  {'object_list': equipment_type})


def error_404_view(request, exception):
    return render(request, '404.html', status=404)
