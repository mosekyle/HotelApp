from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BookingForm
from .models import Booking
from .forms import ContactForm


def index(request):
    return render(request, 'index.html')
def room(request):
    return render(request, 'room.html')
def service(request):
    return render(request, 'service.html')
def team(request):
    return render(request, 'team.html')
def testimonial(request):
    return render(request, 'testimonial.html')
def booking(request):
    return render(request, 'booking.html')
def about(request):
    return render(request, 'about.html')  # Render about.html
def contact(request):
    return render(request, 'contact.html')



def global_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save()  # Save the booking instance
            messages.success(request, 'Booking successful!')
            return redirect('booking_receipt', booking_id=booking.id)  # Redirect to receipt page
    else:
        form = BookingForm()

    return render(request, 'booking.html', {'form': form})


from django.shortcuts import get_object_or_404

def booking_receipt(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)  # Retrieve the booking instance
    return render(request, 'receipt.html', {'booking': booking})




def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save to the database
            messages.success(request, "Thank you for contacting us! We will get back to you shortly.")
            return redirect('contact')  # Redirect to the same page or another page
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})


