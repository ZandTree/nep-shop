from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path("<int:pk>/",views.ProfileInfo.as_view(),name='profile-info'),
    #add user.id by account-overview
    path("account-overview/",views.AccountOverview.as_view(),name='account-info'),

]
