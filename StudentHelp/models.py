from datetime import datetime, date

from django.db import models
from django.contrib.auth.models import User

class Poste(models.Model):
    TYPE_CHOICES = [(0, 'Offre'), (1, 'Demande')]
    image = models.ImageField(blank=True)
    type = models.IntegerField(choices=TYPE_CHOICES, default=0)
    date = models.DateField(default=date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    likes = models.IntegerField(default=0)
    caption = models.CharField(max_length=10000, verbose_name="Caption", null=True)
    is_transport = models.BooleanField(default=False)
    is_Recommandation = models.BooleanField(default=False)
    is_Logement = models.BooleanField(default=False)
    is_Stage = models.BooleanField(default=False)
    is_EvenSocial = models.BooleanField(default=False)
    is_EvenClub = models.BooleanField(default=False)

    def get_specific_attrs(self):
        if hasattr(self, 'transport'):
            return {
                'départ': self.transport.départ,
                'destination': self.transport.destination,
                'heure_dep': self.transport.heure_dep,
                'nbre_sièges': self.transport.nbre_sièges,
                'contactInfo': self.transport.contactInfo
            }
        elif hasattr(self, 'recommandation'):
            return {
                'texte': self.recommandation.texte
            }
        elif hasattr(self, 'logement'):
            return {
                'localisation': self.logement.localisation,
                'description': self.logement.description,
                'contactInfo': self.logement.contactInfo
            }
        elif hasattr(self, 'stage'):
            return {
                'typeStg': self.stage.get_typeStg_display(),
                'société': self.stage.société,
                'durée': self.stage.durée,
                'sujet': self.stage.sujet,
                'contactInfo': self.stage.contactInfo,
                'spécialité': self.stage.spécialité
            }
        elif hasattr(self, 'evensocial'):
            return {
                'intitulé_es': self.evensocial.intitulé_es,
                'description_es': self.evensocial.description_es,
                'lieu_es': self.evensocial.lieu_es,
                'contactInfo_es': self.evensocial.contactInfo_es,
                'prix_es': self.evensocial.prix_es
            }
        elif hasattr(self, 'evenclub'):
            return {
                'intitulé_ev': self.evenclub.intitulé_ev,
                'description_ev': self.evenclub.description_ev,
                'lieu_ev': self.evenclub.lieu_ev,
                'contactInfo_ev': self.evenclub.contactInfo_ev,
                'club_ev': self.evenclub.club_ev
            }
        else:
            return {}

    def __str__(self):
        return f"{self.get_type_display()} {self.date} {self.user.username}"

    def __str__(self):
        return self.user.username

class Recommandation(Poste):
    texte = models.CharField(max_length=100)   

    def __str__(self):
        return f"{super().__str__()} {self.texte}"

class Transport(Poste):
    départ = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)
    heure_dep = models.TimeField(default=datetime.now)
    nbre_sièges = models.IntegerField()
    contactInfo = models.CharField(max_length=8)

    def __str__(self):
        return f"{super().__str__()} {self.départ} {self.destination} {self.heure_dep} {self.nbre_sièges} {self.contactInfo}"

class Logement(Poste):
    localisation = models.CharField(max_length=20)   
    description = models.CharField(max_length=500)   
    contactInfo = models.CharField(max_length=8)

    def __str__(self):
        return f"{super().__str__()} {self.localisation} {self.description} {self.contactInfo}"

class Stage(Poste):
    TYPE_CHOICES = [(1,'Ouvrier'), (2,'Technicien'), (3,'PFE')]
    typeStg = models.IntegerField(choices=TYPE_CHOICES, default=1)
    société = models.CharField(max_length=50)   
    durée = models.IntegerField()  # en mois
    sujet = models.CharField(max_length=100) 
    contactInfo = models.CharField(max_length=8)
    spécialité = models.CharField(max_length=50)

    def __str__(self):
        return f"{super().__str__()} {self.get_typeStg_display()} {self.société} {self.durée} {self.sujet} {self.contactInfo} {self.spécialité}"

class EvenSocial(Poste):
    intitulé_es = models.CharField(max_length=100)
    description_es = models.CharField(max_length=500)
    lieu_es = models.CharField(max_length=100)
    contactInfo_es = models.CharField(max_length=8)
    prix_es = models.DecimalField(max_digits=10, decimal_places=3, default=0.0)

    def __str__(self):
        return f"{self.prix_es}"


class EvenClub(Poste):
    intitulé_ev = models.CharField(max_length=100)
    description_ev = models.CharField(max_length=500)
    lieu_ev = models.CharField(max_length=100)
    contactInfo_ev = models.CharField(max_length=8)
    club_ev = models.CharField(max_length=50, default='Default Club Name')

    def __str__(self):
        return f"{self.club_ev}"

class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile_pciture", null=True, default="default.jpg")
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    bio = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    poste = models.ForeignKey(Poste, related_name='likes_received', on_delete=models.CASCADE, null=True)

class Comment(models.Model):
    post = models.ForeignKey(Poste, on_delete=models.CASCADE, related_name="comment")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True, null=True)

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']