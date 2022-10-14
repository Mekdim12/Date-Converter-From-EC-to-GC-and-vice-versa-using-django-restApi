
from django.urls import path
from . import views
urlpatterns = [

    path('', views.api_Recview, name="api_review"),
    path('Date-retiver/<slug:dates>/<str:dateFormatted>/', views.dateRetriver, name="date_retiriver"),
    

]
