from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView
from main.forms import ContactForm
from django.contrib import messages
from django.shortcuts import get_object_or_404

from main.models import Program, SummitDay, Speaker, Sponsor

# Create your views here.

class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['summit_day_list'] = SummitDay.objects.values('date').order_by('date').all()
        context['day_one_event_list'] = Program.objects.filter(day=1, category='major').order_by('start_time').all()[:6]
        context['day_two_event_list'] = Program.objects.filter(day=2, category='major').order_by('start_time').all()[:6]
        context['speaker_list'] = Speaker.objects.filter(category='major').all()[:5]
        context['sponsor_list'] = Sponsor.objects.all()
        return context


class SpeakerListView(ListView):
    model = Speaker


def prefix_254(number):
    phone = '254'+number.lstrip('0')
    return phone

def contact(request):
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})



