from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
from .forms import EventForm

# READ - List of Events
def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

# CREATE - Add New Event
def event_create(request):
    form = EventForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('event_list')
    return render(request, 'events/event_form.html', {'form': form})

# UPDATE - Edit Event
def event_update(request, pk):
    event = get_object_or_404(Event, pk=pk)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('event_list')
    return render(request, 'events/event_form.html', {'form': form})

# DELETE - Remove Event
def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
    return render(request, 'events/event_confirm_delete.html', {'event': event})