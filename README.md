# Django-Food-Pickup-Volunteer-App
A mock volunteer app where volunteers can select which location and which date they are available for various food pickup locations to pickup food surplus and deliver to designated centers

![Image of admin adding new events](https://raylow00.github.com/images/Screenshot_1.png)
![Image of users registering by date selection](https://raylow00.github.com/images/Screenshot_2.png)
![Image of events page](https://raylow00.github.com/images/Screenshot_3.png)

Users can:
- sign up and log in to own account
- view different food pickup events (Name, Location, Address, Days, Time and Number of volunteers)
- register for events by choosing a date
- delete events if they are not interested (a deadline to delete events coming to a future update)
- view registered events
- mark complete for events by entering a PIN number given by the admin

Admin can:
- do everything a user can
- add events
- generate a PIN number for volunteers to verify that they have completed their task
- update event details
- delete events entirely


What I Learnt:
- how to initialize Django admin and Django authentication for users and admin
- how to use Django PostgreSQL database
- using a datepicker specifically for Django dates for the addition of new events by admin
- Django PostgreSQL foreign key for different tables
