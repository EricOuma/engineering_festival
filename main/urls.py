from django.urls import path

from main import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('contact', views.contact, name="contact"),
    path('speakers', views.SpeakerListView.as_view(), name="speakers"),
]