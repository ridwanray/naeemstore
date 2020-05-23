from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name='main'

urlpatterns = [
    url( 'admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^about$', views.about, name='about'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^faqs$', views.faqs, name='faqs'),
    url(r'^enquiry$', views.enquiry, name='enquiry'),
    url(r'^category$', views.category, name='category'),
    url(r'^review$', views.review, name='review'),
]


 # RegistrationView.as_view(form_class=RegistrationFormTOSAndEmail), 
  #  name='registration_register'