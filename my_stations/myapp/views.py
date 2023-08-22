from django.shortcuts import render, get_object_or_404, redirect
from .models import MonitoringStation, EquipmentType
from django import forms
from django.views import View


class MyappView(View):
    def get(self, request):
        return render(request, 'myapp.html')


class MonitoringStationsView(View):
    def get(self, request):
        monitoring_stations = MonitoringStation.objects.all()
        return render(request, 'stations/monitoring_stations.html', {'object_list': monitoring_stations})


class AddMonitoringStationView(View):
    def get(self, request):
        form = MonitoringStationForm()
        return render(request, 'stations/add_monitoring_station.html', {'form': form})

    def post(self, request):
        form = MonitoringStationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('monitoring_stations')
        return render(request, 'stations/add_monitoring_station.html', {'form': form})


class EditMonitoringStationView(View):
    def get(self, request, pk):
        station = get_object_or_404(MonitoringStation, pk=pk)
        form = MonitoringStationForm(instance=station)
        return render(request, 'stations/edit_monitoring_station.html', {'form': form})

    def post(self, request, pk):
        station = get_object_or_404(MonitoringStation, pk=pk)
        form = MonitoringStationForm(request.POST, instance=station)
        if form.is_valid():
            form.save()
            return redirect('monitoring_stations')
        return render(request, 'stations/edit_monitoring_station.html', {'form': form})


class DeleteMonitoringStationView(View):
    def get(self, request, pk):
        station = get_object_or_404(MonitoringStation, pk=pk)
        return render(request, 'stations/delete_monitoring_station.html', {'station': station})

    def post(self, request, pk):
        station = get_object_or_404(MonitoringStation, pk=pk)
        station.delete()
        return redirect('monitoring_stations')


class MonitoringStationForm(forms.ModelForm):
    class Meta:
        model = MonitoringStation
        fields = '__all__'


class EquipmentTypeForm(forms.ModelForm):
    class Meta:
        model = EquipmentType
        exclude = ['last_update']


class EquipmentTypeView(View):
    def get(self, request):
        equipment_type = EquipmentType.objects.all()
        return render(request, 'equipment/equipment_type.html', {'object_list': equipment_type})


class EditEquipmentTypeView(View):
    def get(self, request, pk):
        equipment = get_object_or_404(EquipmentType, pk=pk)
        form = EquipmentTypeForm(instance=equipment)
        return render(request, 'equipment/edit_equipment_type.html', {'form': form})

    def post(self, request, pk):
        equipment = get_object_or_404(EquipmentType, pk=pk)
        form = EquipmentTypeForm(request.POST, instance=equipment)
        if form.is_valid():
            form.save()
            return redirect('equipment_type')
        return render(request, 'equipment/edit_equipment_type.html', {'form': form})


class DeleteEquipmentTypeView(View):
    def get(self, request, pk):
        equipment = get_object_or_404(EquipmentType, pk=pk)
        return render(request, 'equipment/delete_equipment_type.html', {'equipment': equipment})

    def post(self, request, pk):
        equipment = get_object_or_404(EquipmentType, pk=pk)
        equipment.delete()
        return redirect('equipment_type')


class AddEquipmentTypeView(View):
    def get(self, request):
        form = EquipmentTypeForm()
        return render(request, 'equipment/add_equipment_type.html', {'form': form})

    def post(self, request):
        form = EquipmentTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipment_type')
        return render(request, 'equipment/add_equipment_type.html', {'form': form})


class Error404View(View):
    def get(self, request, exception):
        return render(request, '404.html', status=404)
