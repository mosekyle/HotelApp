from .forms import BookingForm

def global_booking_form(request):
    return {'booking_form': BookingForm()}
