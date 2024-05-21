from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 



class UserRegistrationForm(UserCreationForm): 
    first_name = forms.CharField(label='Prénom') 
    last_name = forms.CharField(label='Nom') 
    email = forms.EmailField(label='Adresse e-mail') 
    class Meta(UserCreationForm.Meta): 
        model = User 
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email')

class NewPostForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    caption = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Caption'}), required=True)
    type = forms.ChoiceField(choices=[(0,'Offre'), (1,'Demande')], widget=forms.Select(attrs={'class': 'input', 'placeholder': 'Type'}), required=True)
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'input', 'placeholder': 'Date', 'type': 'date'}), required=True)

    class Meta:
        model = Poste  
        fields = ['image', 'caption', 'type', 'date']

class RecommandationFrom(forms.ModelForm):
    image = forms.ImageField(required=False)
    caption = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Caption'}), required=True)
    type = forms.ChoiceField(choices=[(0,'Offre'), (1,'Demande')], widget=forms.Select(attrs={'class': 'input', 'placeholder': 'Type'}), required=True)
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'input', 'placeholder': 'Date', 'type': 'date'}), required=True)

    texte = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Texte'}), required=True)
    
    class Meta:
        model = Recommandation
        fields = ['image', 'caption', 'type', 'date', 'texte']
        
class TransportForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    caption = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Caption'}), required=True)
    type = forms.ChoiceField(choices=[(0,'Offre'), (1,'Demande')], widget=forms.Select(attrs={'class': 'input', 'placeholder': 'Type'}), required=True)
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'input', 'placeholder': 'Date', 'type': 'date'}), required=True)

    départ = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Départ'}), required=True)
    destination = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Destination'}), required=True)
    heure_dep = forms.TimeField(widget=forms.TimeInput(attrs={'class': 'input', 'placeholder': 'Heure Départ', 'type': 'time'}), required=True)
    nbre_sièges = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'input', 'placeholder': 'Nombre de sièges'}), required=True)
    contactInfo = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Contact Info'}), required=True)

    class Meta:
        model = Transport  
        fields = ['image', 'caption', 'type', 'date','départ','destination','heure_dep','nbre_sièges','contactInfo']


class LogementForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    caption = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Caption'}), required=True)
    type = forms.ChoiceField(choices=[(0,'Offre'), (1,'Demande')], widget=forms.Select(attrs={'class': 'input', 'placeholder': 'Type'}), required=True)
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'input', 'placeholder': 'Date', 'type': 'date'}), required=True)

    localisation = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Localisation'}),
        required=True
    )
    description = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Description'}),
        required=True
    )
    contactInfo = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Contact Info'}),
        required=True
    )

    class Meta:
        model = Logement  
        fields = ['image', 'caption', 'type', 'date','localisation','description','contactInfo']



class StageForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    caption = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Caption'}), required=True)
    type = forms.ChoiceField(choices=[(0,'Offre'), (1,'Demande')], widget=forms.Select(attrs={'class': 'input', 'placeholder': 'Type'}), required=True)
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'input', 'placeholder': 'Date', 'type': 'date'}), required=True)

    typeStg = forms.ChoiceField(
        choices=[(1, 'Ouvrier'), (2, 'Technicien'), (3, 'PFE')],
        widget=forms.Select(attrs={'class': 'input', 'placeholder': 'Type de Stage'}),
        required=True
    )
    société = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Société'}),
        required=True
    )
    durée = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'input', 'placeholder': 'Durée (en mois)'}),
        required=True
    )
    sujet = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Sujet'}),
        required=True
    )
    contactInfo = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Contact Info'}),
        required=True
    )
    spécialité = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Spécialité'}),
        required=True
    )

    class Meta:
        model = Stage  
        fields = ['image', 'caption', 'type', 'date','typeStg','société','durée','sujet','contactInfo','spécialité']

    

class EvenSocialForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    caption = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Caption'}), required=True)
    type = forms.ChoiceField(choices=[(0,'Offre'), (1,'Demande')], widget=forms.Select(attrs={'class': 'input', 'placeholder': 'Type'}), required=True)
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'input', 'placeholder': 'Date', 'type': 'date'}), required=True)

    intitulé_es = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Intitulé'}),
        required=True
    )
    description_es = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Description'}),
        required=True
    )
    lieu_es = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Lieu'}),
        required=True
    )
    contactInfo_es = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Contact Info'}),
        required=True
    )
    prix_es = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'input', 'placeholder': 'Prix'}),
        required=True
    )

    class Meta:
        model = EvenSocial  
        fields = ['image', 'caption', 'type', 'date','intitulé_es','description_es','lieu_es','contactInfo_es','prix_es']

   

class EvenClubForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    caption = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Caption'}), required=True)
    type = forms.ChoiceField(choices=[(0,'Offre'), (1,'Demande')], widget=forms.Select(attrs={'class': 'input', 'placeholder': 'Type'}), required=True)
    date = forms.DateField(widget=forms.DateInput(attrs={'class': 'input', 'placeholder': 'Date', 'type': 'date'}), required=True)

    intitulé_ev = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Intitulé'}),
        required=True
    )
    description_ev = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Description'}),
        required=True
    )
    lieu_ev = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Lieu'}),
        required=True
    )
    contactInfo_ev = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Contact Info'}),
        required=True
    )
    club_ev = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Club'}),required=True )

    class Meta:
        model = EvenClub  
        fields = ['image', 'caption', 'type', 'date','intitulé_ev','description_ev','lieu_ev','contactInfo_ev','club_ev']


class EditProfileForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'First Name'}), required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Last Name'}), required=True)
    bio = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Bio'}), required=True)
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Address'}), required=True)

    class Meta:
        model = Profile
        fields = ['image', 'first_name', 'last_name', 'bio', 'location']

class NewCommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Write comment'}), required=True)
    
    class Meta:
        model = Comment
        fields = ['body']