from django.urls import path,include
from .views import verify
from .views import register
urlpatterns = [
    path('verify',verify),
    path('reg',register),

]