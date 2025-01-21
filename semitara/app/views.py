from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, LaundryBookingForm
from .models import LaundryBooking
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin



# Home and About Page Views
class HomePageView(TemplateView):
    template_name = 'app/home.html'
    
class AboutPageView(TemplateView):
    template_name = 'app/about.html'

# Custom User Signup View (Create)
class CustomUserSignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')  # Redirect to home page after successful signup

    def form_valid(self, form):
        # Save the new user and log them in after signup
        user = form.save()
        login(self.request, user)  # Log in the user automatically
        return super().form_valid(form)


# Laundry Booking Views
# List of all laundry bookings (Read)
class LaundryBookingListViewAll(ListView):
    model = LaundryBooking
    template_name = 'laundry/laundrybooking_list_all.html'
    context_object_name = 'bookingall'

    def get_queryset(self):
        return LaundryBooking.objects.all()  # Show all bookings

class LaundryBookingListView(ListView):
    model = LaundryBooking
    template_name = 'laundry/laundrybooking_list.html'
    context_object_name = 'bookings'
    
    def get_queryset(self):
        # Ensure the user is authenticated
        if self.request.user.is_authenticated:
            return LaundryBooking.objects.filter(user=self.request.user)
        else:
            return LaundryBooking.objects.none() 
# Create a new laundry booking (Create)class LaundryBookingCreateView(LoginRequiredMixin, CreateView):
class LaundryBookingCreateView(LoginRequiredMixin, CreateView):
    model = LaundryBooking
    form_class = LaundryBookingForm
    template_name = 'laundry/laundrybooking_form.html'
    success_url = reverse_lazy('laundrybooking_list')  # Redirect to booking list after creation

    def form_valid(self, form):
        form.instance.user = self.request.user  # Assign the logged-in user to the booking
        return super().form_valid(form)

# Update an existing laundry booking (Update)
class LaundryBookingUpdateView(UpdateView):
    model = LaundryBooking
    form_class = LaundryBookingForm
    template_name = 'laundry/laundrybooking_form.html'
    success_url = reverse_lazy('laundrybooking_list_all')  # Redirect to booking list after update

# Delete a laundry booking (Delete)
class LaundryBookingDeleteView(DeleteView):
    model = LaundryBooking
    template_name = 'laundry/laundrybooking_confirm_delete.html'
    success_url = reverse_lazy('laundrybooking_list')  # Redirect to booking list after deletion

# Show details of a specific laundry booking (Read)
class LaundryBookingDetailView(DetailView):
    model = LaundryBooking
    template_name = 'laundry/laundrybooking_detail.html'
    context_object_name = 'booking'

from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    logout(request)  # Clear the session
    return redirect('home')  # Redirect to home page after logout

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import LaundryBooking

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')  # Replace 'contact' with the name of your contact page URL
    else:
        form = ContactForm()

    return render(request, 'registration/contact.html', {'form': form})

from django.shortcuts import render
from .models import LaundryBooking

def admin_dashboard(request):
    messages = Contact.objects.all() 
    bookingall = LaundryBooking.objects.all()
    return render(request, 'registration/admin_dashboard.html', {'messages': messages, 'bookingall': bookingall})

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Contact
from django.conf import settings
from django.contrib import messages
def send_reply(request, message_id):
    if request.method == 'POST':
        reply_message = request.POST.get('reply_message')
        try:
            contact_message = Contact.objects.get(id=message_id)
            # Send the email
            subject = f"Reply to your message: {contact_message.name}"
            body = f"Hello {contact_message.name},\n\n{reply_message}"
            from_email = settings.EMAIL_HOST_USER
            to_email = contact_message.email
            send_mail(subject, body, from_email, [to_email])

            # Update status
            contact_message.replied = True
            contact_message.save()

            messages.success(request, "Your reply has been sent.")
        except Contact.DoesNotExist:
            messages.error(request, "Message not found.")
    return redirect('admin_dashboard')


