from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('add/', ajout_plaintes, name='ajout_plaintes'),
    path('modifier/<int:report_id>/', modifier, name='modifier'),
    path('supp/<int:report_id>/', supp, name='supp'),
    path('acc', accueil, name='accueil'),
    path('detail/<int:report_id>/', detail_plainte, name='detail_plainte'),

]
