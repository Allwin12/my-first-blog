from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('hi/',views.contact,name='hi'),
    path('resume/',views.resume,name='resume'),
    path('resume/www.allwin12.pythonanywhere.com',views.home,name='home'),
    path('feedback/',views.feedback,name='feedback'),
    path('blog/',views.blog,name='blog'),
    path('wallethome/',views.wallethome,name='wallet'),
    path('wallethome/wallet/',views.wallet,name='wallet'),
    path('wallet/',views.wallet,name='wallet'),
    path('wallethome/import/',views.importwallet,name='importwallet')
]