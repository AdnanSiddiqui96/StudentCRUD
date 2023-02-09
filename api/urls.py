from django.urls import path,include
from api .views import*
urlpatterns = [
    path('student',studentcrud.as_view())
]