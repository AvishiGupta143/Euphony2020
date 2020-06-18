from django.contrib import admin
from .models import Images, Events, Branch, Team, Domain, Gallery, Profile, EventForm, Resets, DeletedAccounts

admin.site.register(Images)
admin.site.register(Events)
admin.site.register(Branch)
admin.site.register(Profile)
admin.site.register(EventForm)
admin.site.register(Team)
admin.site.register(Domain)
admin.site.register(Resets)
admin.site.register(DeletedAccounts)
admin.site.register(Gallery)
