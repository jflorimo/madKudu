from django.urls import path
from . import views

urlpatterns = [
    # django,
    # debug
    path("debug/", views.DebugAPI.as_view()),
]
