from django.urls import path

from .views import NoteView

app_name = "tgnotes"

urlpatterns = [
    path('tgnotes/', NoteView.as_view()),
    path('tgnotes/<int:pk>', NoteView.as_view())
]
