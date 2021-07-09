from django.contrib import admin
from django.urls import path
from .views import SetEvent
from .views import SetNote
from .views import NoteList
from .views import EventList
from .views import ok

urlpatterns = [
    path('notes',NoteList.as_view()),
    path('events',EventList.as_view()),
    path('set_notes',SetNote.as_view()),
    path('set_events',SetEvent.as_view()),
    path('ok',ok)
]
