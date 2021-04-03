from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Poll

# Create your views here.


class PollListView(ListView):
    template_name = 'poll_list.html'
    context_object_name = 'polls'
    model = Poll


class PollDetailView(DetailView):
    model = Poll
    template_name = 'poll_detail.html'
    context_object_name = 'poll'
