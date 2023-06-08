from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_all_Auto),
    path('traitement/', views.traitement), 
    path('delete_auto/<int:id>/', views.delete_Auto),
    path('update_auto/<int:id>/',views.update_Auto),
    path('view_auto/<int:id>/', views.view_Auto),
    path('add_auto/', views.add_Auto),
    path('traitement_update/<int:id>/', views.traitement_update)
]