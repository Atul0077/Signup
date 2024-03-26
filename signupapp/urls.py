# signupapp/urls.py
from django.urls import path
from .views import signup, cancel

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('cancel/', cancel, name='cancel'),  # Add a cancel URL
    # Add other URLs as needed
]
