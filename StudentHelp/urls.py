from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('post/newPost/', views.newPost, name= 'newPost'),
    path('post/newRecommandation/', views.newRecommandation, name='newRecommandation'),
    path('post/newTransport/', views.newTransport, name='newTransport'),
    path('post/newLogement/', views.newLogement, name='newLogement'),
    path('post/newStage/', views.newStage, name='newStage'),
    path('post/newEvenSocial/', views.newEvenSocial, name='newEvenSocial'),
    path('post/newEvenClub/', views.newEvenClub, name='newEvenClub'),

    path('post/<int:post_id>/',views.PostDetail, name='post-details'),
    path('post/editRecommandation/<int:pk>/', views.edit_recommandation, name='editRecommandation'),
    path('post/editTransport/<int:pk>/', views.edit_transport, name='editTransport'),
    path('post/editLogement/<int:pk>/', views.edit_logement, name='editLogement'), 
    path('post/editStage/<int:pk>/', views.edit_stage, name='editStage'),
    path('post/editEvenSocial/<int:pk>/', views.edit_even_social, name='editEvenSocial'),
    path('post/editEvenClub/<int:pk>/', views.edit_even_club, name='editEvenClub'),
    
    path('<int:pk>/delete/', views.DeletePost.as_view(), name='deletePost'),
    path('post/<int:post_id>/like', views.like, name='like'),
    path('notifications/', views.show_notifications, name='notifications'),

    path('<username>/', views.UserProfile, name='profile'),

    path('<str:username>/editProfile/', views.UpdateProfile.as_view(), name='editProfile'),



]

