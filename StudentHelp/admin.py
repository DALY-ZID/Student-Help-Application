from django.contrib import admin
from .models import Poste, Like, Recommandation, Transport, Logement, Stage, EvenClub, EvenSocial, Profile, Comment
# Register your models here.
# admin.site.register(User)
admin.site.register(Poste)
# admin.site.register(Réaction)
admin.site.register(Recommandation)
admin.site.register(Transport)
admin.site.register(Logement)
admin.site.register(Stage)
admin.site.register(EvenSocial)
admin.site.register(EvenClub)
#admin.site.register(Evènement)
admin.site.register(Like)
admin.site.register(Profile)
admin.site.register(Comment)