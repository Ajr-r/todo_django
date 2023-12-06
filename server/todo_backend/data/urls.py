from django.urls import path
from .views import create
from .views import view
from .views import delete
from .views import test
from .views import capi_test

urlpatterns = [
    path('create',create),
    path('view/<str:name_p>',view),
    path('delete/<int:id_p>',delete),
    path('test',test),
    path('ctest',capi_test.as_view())
   

]