from django.shortcuts import render
from .models import Note,Event
from django.http import HttpResponse
from rest_framework import generics
from .serializers import NoteSerializer,EventSerializer
from django.views.generic import CreateView



class SetEvent(CreateView):
    model = Event
    fields = "__all__"
    success_url = 'http://127.0.0.1:8000/game/ok'


class SetNote(CreateView):
    model= Note
    fields = "__all__"
    success_url = 'http://127.0.0.1:8000/game/ok'


class NoteList(generics.ListAPIView):
    queryset = Note.objects.all()
    model = Note
    serializer_class = NoteSerializer

class EventList(generics.ListAPIView):
    queryset = Event.objects.all()
    model = Event
    serializer_class = EventSerializer

def ok(request):
    return HttpResponse("OK")
