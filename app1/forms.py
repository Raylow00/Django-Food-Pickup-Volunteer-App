from django.forms import ModelForm, DateInput, TextInput, SelectMultiple, ChoiceField, CharField
from django.forms import SelectDateWidget
from app1.models import User, Event, Registration
from bootstrap_datepicker_plus import DatePickerInput

'''class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs={'class':'input', 'type':'text', 'placeholder':'Enter a username'}),
            'password1': TextInput(attrs={'class':'input', 'type':'password', 'placeholder':'Enter a password'}),
            'password2': TextInput(attrs={'class':'input', 'type':'password', 'placeholder':'Re-enter the password'}),
        }

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.IC = self.cleaned_data['IC_number']
        if commit:
            user.save()
        return user
'''

class RegistrationForm(ModelForm):
    class Meta:
        model = Registration
        fields = ['date', 'tagged']
        widgets = {
            'user': TextInput(attrs={'class':'input', 'type':'text', 'placeholder':'Enter your name'}),
            'date': DatePickerInput(format='%Y-%m-%d'),
            'tagged': TextInput(attrs={'class':'input', 'type':'text', 'placeholder':"Enter your friends' username to tag them. E.g. Tzuyu, Mina, Sana, MOMO, Nayeon"})
            #'pin': TextInput(attrs={'class':'input', 'type':'text', 'placeholder':'PIN number'}),
        }


class addEventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'location', 'address', 'details_days', 'details_time', 'volunteers', 'pin']
        widgets = {
            'name' : TextInput(attrs={'class':'input', 'type':'text', 'placeholder':'Enter a name for the event'}),
            'location': TextInput(attrs={'class':'input','type':'text','placeholder':'Enter a short name for the location'}),
            'address': TextInput(attrs={'class':'input','type':'text','placeholder':'Enter the full address for the location'}),
            'details_time': TextInput(attrs={'class':'input','type':'text','placeholder':'E.g. 2pm - 5pm on weekdays, 4pm-6pm on weekends'}),
            'volunteers': TextInput(attrs={'class':'input', 'type':'text', 'placeholder':'Enter the number of volunteers needed : 10'}),
            'pin': TextInput(attrs={'class':'input', 'type':'text', 'placeholder':'Enter the confirmation PIN number'}),
        }