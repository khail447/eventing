from core.forms import EventForm
from django.shortcuts import redirect, render
from .forms import EventForm
from .models import Event

# Create your views here.
def frontpage(request):
    events = Event.objects.all()

    context = {
        'events':events
    }
    return render(request, 'frontpage.html', context)

def new_events(request):
    if request.method == 'POST':
        form = EventForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('frontpage')

    else:
        form = EventForm()
    context = {
        'form':form
    }

    return render(request, 'newevent.html', context)