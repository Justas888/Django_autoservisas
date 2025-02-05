from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('automobiliai/', views.automobiliai, name='automobiliai-all'),
    path('automobiliai/<int:automobilis_id>/',
         views.automobilis, name='automobilis-info'),
    path('uzsakymai/',
         views.UzsakymaiListView.as_view(), name='uzsakymai-list'),
    path('uzsakymas/<int:pk>/',
        views.UzsakymasDetailView.as_view(), name='uzsakymas-detail'),

]
