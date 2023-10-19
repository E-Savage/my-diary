from django.shortcuts import render
from django.views.generic import (ListView, DetailView)
from . import Entry

# Create your views here.

class EntryListView(ListView):
    model = Entry
    queryset = Entry.objects.all().order_by("-date_created")

class EntryDetailView(DetailView):
    model = Entry
