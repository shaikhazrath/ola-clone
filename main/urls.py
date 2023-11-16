from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('cars',views.getcars,name='cars'),
    path('moredetails/<int:car_id>/', views.more_details_view, name='moredetails'),

]
