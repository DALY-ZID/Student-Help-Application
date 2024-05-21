from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import resolve, reverse, reverse_lazy
from .models import *
from .forms import NewCommentForm, TransportForm,TransportForm,LogementForm,StageForm,EvenSocialForm,EvenClubForm,EditProfileForm,NewPostForm, RecommandationFrom
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def index(request):
    post_items = Poste.objects.all().order_by('-date')
    
    item_type = request.GET.get('item-type')

    if item_type:  
        if item_type.lower() == '#offre' or item_type.lower() == 'offre':
            post_items = post_items.filter(type=0)
        elif item_type.lower() == 'demande' or item_type.lower() == '#demande':
            post_items = post_items.filter(type=1)

        elif item_type.lower() == '#transport' or item_type.lower() == 'transport':
            post_items = post_items.filter(is_transport=True)

        elif item_type.lower() == '#demande transport' or item_type.lower() == 'demande transport':
            post_items = post_items.filter(is_transport=True,type=1 )

        elif item_type.lower() == '#offre transport' or item_type.lower() == 'offre transport':
            post_items = post_items.filter(is_transport=True,type=0 )

        
        elif item_type.lower() == '#recommandation' or item_type.lower() == 'recommandation':
            post_items = post_items.filter(is_Recommandation=True)
        
        elif item_type.lower() == '#demande recommandation' or item_type.lower() == 'demande recommandation':
            post_items = post_items.filter(is_Recommandation=True,type=1 )

        elif item_type.lower() == '#offre recommandation' or item_type.lower() == 'offre recommandation':
            post_items = post_items.filter(is_Recommandation=True,type=0 )

        elif item_type.lower() == '#logement' or item_type.lower() == 'logement':
            post_items = post_items.filter(is_Logement=True)
        
        elif item_type.lower() == '#offre logement' or item_type.lower() == 'offre logement':
            post_items = post_items.filter(is_Logement=True,type=0 )

        elif item_type.lower() == '#demande logement' or item_type.lower() == 'demande logement':
            post_items = post_items.filter(is_Logement=True,type=1 )

        elif item_type.lower() == '#stage' or item_type.lower() == 'stage':
            post_items = post_items.filter(is_Stage=True)
        
        elif item_type.lower() == '#offre stage' or item_type.lower() == 'offre stage':
            post_items = post_items.filter(is_Stage=True,type=0 )
        
        elif item_type.lower() == '#demande stage' or item_type.lower() == 'demande stage':
            post_items = post_items.filter(is_Stage=True,type=1 )

        elif item_type.lower() == '#eventsocial' or item_type.lower() == 'eventsocial':
            post_items = post_items.filter(is_EvenSocial=True)

        elif item_type.lower() == '#offre eventsocial' or item_type.lower() == 'offre eventsocial':
            post_items = post_items.filter(is_EvenSocial=True,type=0 )

        elif item_type.lower() == '#demande eventsocial' or item_type.lower() == 'demande eventsocial':
            post_items = post_items.filter(is_EvenSocial=True,type=1 )

        elif item_type.lower() == '#eventclub' or item_type.lower() == 'eventclub':
            post_items = post_items.filter(is_EvenClub=True)
        
        elif item_type.lower() == '#offre eventclub' or item_type.lower() == 'offre eventclub':
            post_items = post_items.filter(is_EvenClub=True,type=0 )

        elif item_type.lower() == '#demande eventclub' or item_type.lower() == 'demande eventclub':
            post_items = post_items.filter(is_EvenClub=True,type=1 )

    for post in post_items:
        if isinstance(post, Transport):  
            post.is_transport = True
        if isinstance(post, Recommandation):  
            post.is_Recommandation = True
        if isinstance(post, EvenSocial):
            post.is_EvenSocial = True
        if isinstance(post, EvenClub):
            post.is_EvenClub = True

    context = {
        'post_items': post_items,
    }
    return render(request, 'StudentHelp/index.html', context)



@login_required
def newPost(request):
    user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data.get('image')
            caption = form.cleaned_data.get('caption')
            type = form.cleaned_data.get('type')
            date = form.cleaned_data.get('date') 
            p, created = Poste.objects.get_or_create(image=image,caption=caption, type=type,date=date, user=user)     
            return HttpResponseRedirect(reverse('index'))
    else:
        form = NewPostForm()
    return render(request,'StudentHelp/newPost.html',{'form':form})

@login_required
def newTransport(request):
    user = request.user
    if request.method == 'POST':
        form = TransportForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data.get('image')
            caption = form.cleaned_data.get('caption')
            type = form.cleaned_data.get('type')
            date = form.cleaned_data.get('date')
            départ = form.cleaned_data.get('départ')
            destination = form.cleaned_data.get('destination')
            heure_dep = form.cleaned_data.get('heure_dep')
            nbre_sièges = form.cleaned_data.get('nbre_sièges')
            contactInfo = form.cleaned_data.get('contactInfo')

            p, created = Transport.objects.get_or_create(
                image=image, caption=caption, type=type, date=date,
                user=user, départ=départ, destination=destination, 
                heure_dep=heure_dep, nbre_sièges=nbre_sièges, 
                contactInfo=contactInfo
            )
            if created:
                p.is_transport = True
                p.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = TransportForm()
    return render(request, 'StudentHelp/newTransport.html', {'form': form})


@login_required
def newRecommandation(request):
    user = request.user
    if request.method == 'POST':
        form = RecommandationFrom(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data.get('image')
            caption = form.cleaned_data.get('caption')
            type = form.cleaned_data.get('type')
            date = form.cleaned_data.get('date')
            texte = form.cleaned_data.get('texte')
            
            p, created = Recommandation.objects.get_or_create(
                image=image, caption=caption, type=type, date=date,
                user=user, texte=texte
            )
            if created:
                p.is_Recommandation = True
                p.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = RecommandationFrom()
    return render(request, 'StudentHelp/newRecommandation.html', {'form': form})

@login_required
def newLogement(request):
    user = request.user
    if request.method == 'POST':
        form = LogementForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data.get('image')
            caption = form.cleaned_data.get('caption')
            type = form.cleaned_data.get('type')
            date = form.cleaned_data.get('date')

            localisation = form.cleaned_data.get('localisation')
            description = form.cleaned_data.get('description')
            contactInfo = form.cleaned_data.get('contactInfo')

            p, created = Logement.objects.get_or_create(
                image=image, caption=caption, type=type, date=date,
                user=user, localisation=localisation,description=description,
                contactInfo=contactInfo
            )
            if created:
                p.is_Logement = True
                p.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = LogementForm()
    return render(request, 'StudentHelp/newLogement.html', {'form': form})

@login_required
def newStage(request):
    user = request.user
    if request.method == 'POST':
        form = StageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data.get('image')
            caption = form.cleaned_data.get('caption')
            type = form.cleaned_data.get('type')
            date = form.cleaned_data.get('date')

            typeStg = form.cleaned_data.get('typeStg')
            société = form.cleaned_data.get('société')
            durée = form.cleaned_data.get('durée')
            sujet = form.cleaned_data.get('sujet')
            contactInfo = form.cleaned_data.get('contactInfo')
            spécialité = form.cleaned_data.get('spécialité')

            p, created = Stage.objects.get_or_create(
                image=image, caption=caption, type=type, date=date,
                user=user, typeStg=typeStg,société=société,
                durée=durée, sujet=sujet,
                contactInfo=contactInfo,
                spécialité=spécialité,
            )
            if created:
                p.is_Stage = True
                p.save()            
                

            return HttpResponseRedirect(reverse('index'))
    else:
        form = StageForm()
    return render(request, 'StudentHelp/newStage.html', {'form': form})

@login_required
def newEvenSocial(request):
    user = request.user
    if request.method == 'POST':
        form = EvenSocialForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data.get('image')
            caption = form.cleaned_data.get('caption')
            type = form.cleaned_data.get('type')
            date = form.cleaned_data.get('date')
        
            intitulé_es = form.cleaned_data.get('intitulé_es')
            description_es = form.cleaned_data.get('description_es')
            lieu_es = form.cleaned_data.get('lieu_es')
            contactInfo_es = form.cleaned_data.get('contactInfo_es')
            prix_es = form.cleaned_data.get('prix_es')

            p, created = EvenSocial.objects.get_or_create(
                image=image, caption=caption, type=type, date=date,
                user=user, intitulé_es=intitulé_es,
                description_es=description_es,
                lieu_es=lieu_es,
                contactInfo_es=contactInfo_es,
                prix_es=prix_es,
            )
            if created:
                p.is_EvenSocial = True
                p.save() 
        
            return HttpResponseRedirect(reverse('index'))
    else:
        form = EvenSocialForm()
    return render(request, 'StudentHelp/new_even_social.html', {'form': form})

@login_required
def newEvenClub(request):
    user = request.user
    if request.method == 'POST':
        form = EvenClubForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data.get('image')
            caption = form.cleaned_data.get('caption')
            type = form.cleaned_data.get('type')
            date = form.cleaned_data.get('date')

            intitulé_ev = form.cleaned_data.get('intitulé_ev')
            description_ev = form.cleaned_data.get('description_ev')
            lieu_ev = form.cleaned_data.get('lieu_ev')
            contactInfo_ev = form.cleaned_data.get('contactInfo_ev')
            club_ev = form.cleaned_data.get('club_ev')

            p, created = EvenClub.objects.get_or_create(
                image=image, caption=caption, type=type, date=date,
                user=user, intitulé_ev=intitulé_ev,
                description_ev=description_ev,
                lieu_ev=lieu_ev,
                contactInfo_ev=contactInfo_ev,
                club_ev=club_ev
            )
            if created:
                p.is_EvenClub = True
                p.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = EvenClubForm()
    return render(request, 'StudentHelp/new_even_club.html', {'form': form})


@login_required
def like(request, post_id):
    post = Poste.objects.get(id=post_id)
    current_likes = post.likes
    user = request.user
    liked = Like.objects.filter(user=user, poste_id=post.id).count()

    if not liked:
        Like.objects.create(user=user, poste_id=post.id)
        current_likes += 1

        # Créer une notification pour le propriétaire de la publication
        if post.user != user:
            Notification.objects.create(
                user=post.user,
                content=f"{user.username} a aimé votre publication."
            )

    else:
        Like.objects.filter(user=user, poste_id=post.id).delete()
        current_likes -= 1

    post.likes = current_likes
    post.save()
    return HttpResponseRedirect(reverse('index'))

@login_required
def PostDetail(request, post_id):
    user = request.user
    post = get_object_or_404(Poste, id=post_id)
    comments = Comment.objects.filter(post=post).order_by('-date')
    comment_count = comments.count()

    if request.method == "POST":
        form = NewCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = user
            comment.save()

            # Créer une notification pour le propriétaire de la publication
            if post.user != user:
                Notification.objects.create(
                    user=post.user,
                    content=f"{user.username} a commenté votre publication."
                )

            return HttpResponseRedirect(reverse('post-details', args=[post.id]))
    else:
        form = NewCommentForm()

    context = {
        'post': post,
        'form': form,
        'comments': comments,
        'comment_count': comment_count
    }

    return render(request, 'StudentHelp/detailsPost.html', context)
    
class DeletePost(LoginRequiredMixin, DeleteView):
    model = Poste
    success_url = reverse_lazy('index')  
    pk_url_kwarg = 'pk'

    def dispatch(self, request, *args, **kwargs):
        post = self.get_object()
        if post.user != self.request.user:
            return redirect('index')  
        return super().dispatch(request, *args, **kwargs)  


def UserProfile(request, username):
    Profile.objects.get_or_create(user=request.user)
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get(user=user)
    posts = Poste.objects.filter(user=user).order_by('-date')

    posts_count = Poste.objects.filter(user=user).count()
    likes_count_dict = {}
    for post in posts:
        likes_count_dict[post.id] = Like.objects.filter(poste=post).count()
    paginator = Paginator(posts, 8)
    page_number = request.GET.get('page')
    posts_paginator = paginator.get_page(page_number)

    context = {
        'posts': posts,
        'profile':profile,
        'posts_count':posts_count,
        'posts_paginator':posts_paginator,
        'likes_count_dict':likes_count_dict,
    }
    return render(request, 'StudentHelp/profile.html', context)


@method_decorator(login_required, name='dispatch')
class UpdateProfile(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'StudentHelp/editProfile.html'
    form_class = EditProfileForm

    def get_success_url(self):
        username = self.kwargs['username']
        return reverse_lazy('profile', kwargs={'username': username})
    
    def get_object(self, queryset=None):
        username = self.kwargs.get('username')
        user = get_object_or_404(User, username=username)
        profile = user.profile
        return profile
    
    def dispatch(self, request, *args, **kwargs):
        username = self.kwargs.get('username')
        if username != self.request.user.username:
            messages.error(request, "You are not allowed to edit this profile.")
            return redirect('profile', username=self.request.user.username)  # Redirect to the user's own profile page or another appropriate page
        return super().dispatch(request, *args, **kwargs)


@login_required
def show_notifications(request):
    user = request.user
    notifications = Notification.objects.filter(user=user)
    return render(request, 'StudentHelp/notification.html', {'notifications': notifications})


# @login_required
# def edit_post(request, post_id):
#     post = get_object_or_404(Poste, id=post_id)
    
#     if request.method == 'POST':
#         form = NewPostForm(request.POST, request.FILES, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('post-details', post_id=post.id)
#     else:
#         form = NewPostForm(instance=post)
#     return render(request, 'edit_post.html', {'form': form})


def edit_recommandation(request, pk):
    recommandation = get_object_or_404(Recommandation, pk=pk)
    if request.method == 'POST':
        form = RecommandationFrom(request.POST, request.FILES, instance=recommandation)
        if form.is_valid():
            form.save()
            return redirect('post-details', post_id=recommandation.id)
    else:
        form = RecommandationFrom(instance=recommandation)
    return render(request, 'StudentHelp/edit_recommandation.html', {'form': form})



def edit_transport(request, pk):
    transport = get_object_or_404(Transport, pk=pk)
    if request.method == 'POST':
        form = TransportForm(request.POST, request.FILES, instance=transport)
        if form.is_valid():
            form.save()
            return redirect('post-details', post_id=transport.id)
    else:
        form = TransportForm(instance=transport)
    return render(request, 'StudentHelp/edit_transport.html', {'form': form, 'transport': transport})


def edit_logement(request, pk):
    logement = get_object_or_404(Logement, pk=pk)
    if request.method == 'POST':
        form = LogementForm(request.POST, request.FILES, instance=logement)
        if form.is_valid():
            form.save()
            return redirect('post-details', post_id=logement.id)
    else:
        form = LogementForm(instance=logement)
    return render(request, 'StudentHelp/edit_logement.html', {'form': form, 'logement': logement})

def edit_stage(request, pk):
    stage = get_object_or_404(Stage, pk=pk)
    if request.method == 'POST':
        form = StageForm(request.POST, request.FILES, instance=stage)
        if form.is_valid():
            form.save()
            return redirect('post-details', post_id=stage.id)
    else:
        form = StageForm(instance=stage)
    return render(request, 'StudentHelp/edit_stage.html', {'form': form, 'stage': stage})

def edit_even_social(request, pk):
    even_social = get_object_or_404(EvenSocial, pk=pk)
    if request.method == 'POST':
        form = EvenSocialForm(request.POST, request.FILES, instance=even_social)
        if form.is_valid():
            form.save()
            return redirect('post-details', post_id=even_social.id)
    else:
        form = EvenSocialForm(instance=even_social)
    return render(request, 'StudentHelp/edit_even_social.html', {'form': form, 'even_social': even_social})



def edit_even_club(request, pk):
    even_club = get_object_or_404(EvenClub, pk=pk)
    if request.method == 'POST':
        form = EvenClubForm(request.POST, request.FILES, instance=even_club)
        if form.is_valid():
            form.save()
            return redirect('post-details', post_id=even_club.id)
    else:
        form = EvenClubForm(instance=even_club)
    return render(request, 'StudentHelp/edit_even_club.html', {'form': form, 'even_club': even_club})
