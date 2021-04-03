from django.shortcuts import redirect, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Poll
from .forms import PollForm

# Create your views here.


class PollListView(ListView):
    template_name = 'poll_list.html'
    context_object_name = 'polls'
    model = Poll


class PollDetailView(DetailView):
    model = Poll
    template_name = 'poll_detail.html'
    context_object_name = 'poll'


class PollCreate(CreateView):
    template_name = 'poll_form.html'
    model = Poll
    form_class = PollForm

    def form_valid(self, form):
        poll = form.save(commit=False)
        poll.save()
        return redirect('poll_list')


class PollUpdate(UpdateView):
    model = Poll
    template_name = 'poll_form.html'
    form_class = PollForm
    context_key = 'poll'

    def get_success_url(self):
        return reverse('poll_detail', kwargs={'pk': self.object.pk})