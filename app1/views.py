from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_POST
from .forms import RegistrationForm, addEventForm
from .models import Event, Registration



# Create your views here.
def signup(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')

    else:
        form = UserCreationForm()

    context = {'form':form}

    return render(request, 'registration/signup.html', context)




def login(request):
    return redirect('login')




def index(request):

    if request.user.is_authenticated:

        events = Event.objects.all()

        context = {'events': events}
    else:
        return redirect('login')

    return render(request, 'app1/index.html', context)




def details(request, event_id):

    details = Event.objects.get(pk=event_id)

    context = {'details': details}

    return render(request, 'app1/details.html', context)




def form(request, details_id):

    events = Event.objects.get(pk=details_id)

    form = RegistrationForm()

    context = { 'form': form, 'events': events }

    return render(request, 'app1/form.html', context)




@require_POST
def register(request, event_name):

    #username = None
    count = 0

    event = Event.objects.get(name=event_name)

    if request.user.is_authenticated:
        USERNAME = request.user.username
    
    form = RegistrationForm(request.POST)
    if form.is_valid():
        try:
            tagged_ = form.cleaned_data['tagged']
            if tagged_ is not None:
                for tagged_user in tagged_:
                    checkUser = User.objects.filter(username=str(tagged_user)).exists()
                    if checkUser:
                        new_register_2 = Registration(
                            user=tagged_user,
                            key=event,
                            date=form.cleaned_data['date'],
                        )
                        new_register_2.save()
                        count += 1
            new_register = Registration(
                user=USERNAME,
                key=event, 
                date=form.cleaned_data['date'],
                tagged=tagged_,
                )
            new_register.save()
            event.volunteers = event.volunteers - (count+1)
            event.save()
            return redirect('profile')
            
            '''
            tagged_ = form.cleaned_data['tagged']
            if tagged_ is not None:
                for tagged_user in tagged_:
                    check_user = User.objects.get(username=tagged_user)
                    if check_user:
                        new_register_2 = Registration(
                            user=tagged_user,
                            key=event,
                            date=form.cleaned_data['date'],
                        )
                        new_register_2.save()
                        count += 1
            new_register = Registration(
                user=username,
                key=event, 
                date=form.cleaned_data['date'],
                tagged=form.cleaned_data['tagged'],
                )
            new_register.save()
            event.volunteers = event.volunteers - (len(count)+1)
            event.save()
            return redirect('profile')
            '''
        except:
            raise ValueError('Problems registering user')
        
    else:
        raise ValueError('There is an error registering you')
    return redirect('profile')





def logout(request):

    logout(request.user)

    return redirect('login')





def addEvent(request):

    if request.user.is_superuser:
            form = addEventForm()

    context = {'form':form}

    return render(request, 'app1/form_admin.html', context)



@require_POST
def add(request):

    if request.method == 'POST':
        form1 = addEventForm(request.POST)
        if form1.is_valid():
            eventName = form1.cleaned_data['name']
            eventLocation = form1.cleaned_data['location']
            eventAddress = form1.cleaned_data['address']
            eventDay = form1.cleaned_data['details_days']
            eventTime = form1.cleaned_data['details_time']
            eventVolunteers = form1.cleaned_data['volunteers']
            
            newEvent = Event(name=eventName, 
                                location=eventLocation, 
                                address=eventAddress, 
                                details_days=eventDay, 
                                details_time=eventTime, 
                                volunteers=eventVolunteers)
            newEvent.save()

    return redirect('index')




def profile(request):

    upcomingEvents = Registration.objects.filter(user=request.user, completed=False)  
    completedEvents = Registration.objects.filter(user=request.user, completed=True)

    context = {'completedEvents':completedEvents, 'upcomingEvents':upcomingEvents}

    return render(request, 'app1/profile.html', context)




def delete(request, id):

    event = Registration.objects.get(pk=id)
    event.delete()

    return redirect('profile')
    

def deleteEvent(request, id):
    event = Event.objects.get(pk=id)
    event.delete()

    return redirect('index')


def updateEvent(request, id):

    event = Event.objects.get(pk=id)

    form = addEventForm()

    context = {'event':event, 'form':form}

    return render(request, 'app1/form_update.html', context)


@require_POST
def update(request, id):
    event = Event.objects.get(pk=id)
    if request.method == 'POST':
        form2 = addEventForm(request.POST)
        if form2.is_valid():
            data = request.POST.copy()  
            event.name = data.get('name')
            event.location = data.get('location')
            event.address = data.get('address')
            event.details_days = form2.cleaned_data['details_days']
            event.details_time = data.get('details_time')
            event.volunteers = data.get('volunteers')
            event.pin = data.get('pin')
            
            event.save()

            return redirect('index')



def markComplete(request, username):
    if request.method == 'POST':
        events = Event.objects.all()
        data = request.POST.copy()
        pin2 = data.get('data')
        for event in events:
            if event.pin is not None:
                if int(event.pin) == int(pin2):
                    user = Registration.objects.get(user=username, key=event, date=date.today())
                    user.completed = True
                    user.save()
                    return redirect('profile')
                else:
                    message = 'PIN number entered is incorrect. Please try again.'
                    context = {'message':message}
                    return render(request, 'app1/profile.html', context)
    return render(request, 'app1/index.html')
