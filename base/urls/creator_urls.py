from base.views import creator_views as views
from django.urls import path


urlpatterns = [
    path('',           views.getCreators,      name = "creators"),
    path('<str:pk>/',  views.getCreator,       name = "creator")
]

