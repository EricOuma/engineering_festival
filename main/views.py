from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView
from main.forms import ContactForm
from django.contrib import messages
from django.shortcuts import get_object_or_404

from main.models import Program, SummitDay, Speaker, Sponsor

from main.sls_calendar import calendar_setup

# Create your views here.

class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['summit_day_list'] = SummitDay.objects.values('date').order_by('date').all()
        context['day_one_event_list'] = Program.objects.filter(day=1).order_by('start_time').all()
        context['day_two_event_list'] = Program.objects.filter(day=2).order_by('start_time').all()
        context['day_three_event_list'] = Program.objects.filter(day=3).order_by('start_time').all()
        context['speaker_list'] = Speaker.objects.all()[:5]
        context['sponsor_list'] = Sponsor.objects.all()
        return context


class SpeakerListView(ListView):
    model = Speaker


class PrivacyView(TemplateView):
    template_name = "privacy.html"

def prefix_254(number):
    phone = '254'+number.lstrip('0')
    return phone

def register(request):
    return render(request, 'register.html')



def contact(request):
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})



# def add_to_calendar(request, event_id):
#     service = calendar_setup()
#     calendarId='882q1makp7mtkq9lvirmqd36ac@group.calendar.google.com'
#     this_event = service.events().get(calendarId = calendarId, eventId=event_id).execute()
#     event = service.events().insert(calendarId='primary', body=this_event).execute()
#     if event:
#         messages.success(request, 'Programme added to your calendar.')
#         return redirect('index')
#     else:
#         messages.info(request, 'There was an error adding the event.')
#         return redirect('index')


