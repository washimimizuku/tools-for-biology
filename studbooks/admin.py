from django.contrib import admin
from studbooks.models import *

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Domain)
admin.site.register(Kingdom)
admin.site.register(Phylum)
admin.site.register(Class)
admin.site.register(Order)
admin.site.register(Family)
admin.site.register(Genus)
admin.site.register(ConservationStatus)
admin.site.register(Species)
admin.site.register(Studbook)
admin.site.register(Specimen)
admin.site.register(EventType)
admin.site.register(Event)