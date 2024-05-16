from django.urls import path
from.views import ResgiterUserView

app_name = 'account'

urlpatterns = [
    path('register/', ResgiterUserView.as_view(),name='register')
]