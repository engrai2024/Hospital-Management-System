from django.shortcuts import render, redirect
from .models import Doctor, Patient, Appointment
from .forms import DoctorForm, PatientForm, AppointmentForm

def home(request):
    return render(request, 'hospital/home.html')

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'hospital/doctor_list.html', {'doctors': doctors})

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'hospital/patient_list.html', {'patients': patients})

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'hospital/appointment_list.html', {'appointments': appointments})

# View for management system
def management_system(request):
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    appointments = Appointment.objects.all()

    if request.method == 'POST':
        if 'doctor_form' in request.POST:
            doctor_form = DoctorForm(request.POST)
            if doctor_form.is_valid():
                doctor_form.save()
                return redirect('management_system')
        elif 'patient_form' in request.POST:
            patient_form = PatientForm(request.POST)
            if patient_form.is_valid():
                patient_form.save()
                return redirect('management_system')
        elif 'appointment_form' in request.POST:
            appointment_form = AppointmentForm(request.POST)
            if appointment_form.is_valid():
                appointment_form.save()
                return redirect('management_system')
    else:
        doctor_form = DoctorForm()
        patient_form = PatientForm()
        appointment_form = AppointmentForm()

    context = {
        'doctors': doctors,
        'patients': patients,
        'appointments': appointments,
        'doctor_form': doctor_form,
        'patient_form': patient_form,
        'appointment_form': appointment_form,
    }
    return render(request, 'hospital/management_system.html', context)

