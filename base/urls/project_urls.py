from django.urls import path
from base.views import project_views as views


urlpatterns = [
    #path('creators/login/',     views.MyTokenObtainPairView.as_view(),  name = 'token_obtain_pair_creator'),
    path('',           views.getProjects,      name = "projects"),
    path('<str:pk>/',  views.getProject,       name = "project")
]

