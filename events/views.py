from django.shortcuts import render, get_object_or_404, redirect
from .models import Event,Category,Participant
from .forms import EventForm,CategoryForm,ParticipantForm
from django.db.models import Count
from django.utils.dateparse import parse_date


# READ - List of Events
def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_list(request):
    # সব event + category আনছি
    events = Event.objects.select_related('category').annotate(
        participant_count=Count('participant')
    )

    # 🟢 ফিল্টার: Category
    category_id = request.GET.get('category')
    if category_id:
        events = events.filter(category_id=category_id)

    # 🟢 ফিল্টার: Date Range
    start_date = parse_date(request.GET.get('start'))
    end_date = parse_date(request.GET.get('end'))

    if start_date and end_date:
        events = events.filter(date__range=(start_date, end_date))

    total_participants = Participant.objects.count()

    return render(request, 'events/event_list.html', {
        'events': events,
        'total_participants': total_participants,
    })

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

# READ - Category List
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'events/category_list.html', {'categories': categories})

# CREATE
def category_create(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('category_list')
    return render(request, 'events/category_form.html', {'form': form})

# UPDATE
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    form = CategoryForm(request.POST or None, instance=category)
    if form.is_valid():
        form.save()
        return redirect('category_list')
    return render(request, 'events/category_form.html', {'form': form})

# DELETE
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'events/category_confirm_delete.html', {'category': category})

# READ - Participant List
def participant_list(request):
    participants = Participant.objects.all()
    return render(request, 'events/participant_list.html', {'participants': participants})

# CREATE
def participant_create(request):
    form = ParticipantForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('participant_list')
    return render(request, 'events/participant_form.html', {'form': form})

# UPDATE
def participant_update(request, pk):
    participant = get_object_or_404(Participant, pk=pk)
    form = ParticipantForm(request.POST or None, instance=participant)
    if form.is_valid():
        form.save()
        return redirect('participant_list')
    return render(request, 'events/participant_form.html', {'form': form})

# DELETE
def participant_delete(request, pk):
    participant = get_object_or_404(Participant, pk=pk)
    if request.method == 'POST':
        participant.delete()
        return redirect('participant_list')
    return render(request, 'events/participant_confirm_delete.html', {'participant': participant})

def event_list(request):
    events = Event.objects.select_related('category').all()
    return render(request, 'events/event_list.html', {'events': events})

def participant_list(request):
    # এখানে prefetch_related ব্যবহার করব
    participants = Participant.objects.prefetch_related('events').all()
    
    return render(request, 'events/participant_list.html', {
        'participants': participants
    })