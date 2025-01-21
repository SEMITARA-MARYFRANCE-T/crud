from django.urls import path 
from django.contrib.auth import views as auth_views
from .views import HomePageView,AboutPageView
from .views import CustomUserSignupView
from .views import LaundryBookingListView, LaundryBookingCreateView, LaundryBookingUpdateView, LaundryBookingDeleteView, LaundryBookingDetailView,LaundryBookingListViewAll
from .views import contact_view
from . import views
from .views import custom_logout

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', custom_logout, name='logout'),
    path('signup/', CustomUserSignupView.as_view(), name='signup'),
    path('bookings/all/', LaundryBookingListViewAll.as_view(), name='laundrybooking_list_all'),
    path('laundry/', LaundryBookingListView.as_view(), name='laundrybooking_list'),
    path('create/', LaundryBookingCreateView.as_view(), name='laundrybooking_create'),
    path('<int:pk>/update/', LaundryBookingUpdateView.as_view(), name='laundrybooking_update'),
    path('<int:pk>/delete/', LaundryBookingDeleteView.as_view(), name='laundrybooking_delete'),
    path('<int:pk>/', LaundryBookingDetailView.as_view(), name='laundrybooking_detail'),
    path('contact/', contact_view, name='contact'),
]

