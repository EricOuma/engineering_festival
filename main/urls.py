from django.urls import path

from main import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('register', views.register, name="register"),
    path('contact', views.contact, name="contact"),
    path('privacy', views.PrivacyView.as_view(), name="privacy"),
    path('speakers', views.SpeakerListView.as_view(), name="speakers"),
    # path('add_to_calendar/<str:event_id>', views.add_to_calendar, name="add_to_calendar"),
]