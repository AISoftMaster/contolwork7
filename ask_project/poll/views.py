from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Poll, Choice
from .forms import PollForm

# Create your views here.


class PollListView(ListView):
    template_name = 'poll_list.html'
    context_object_name = 'polls'
    model = Poll
    paginate_by = 5


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


class PollDelete(DeleteView):
    model = Poll
    template_name = 'poll_delete.html'
    context_object_name = 'poll'
    success_url = reverse_lazy('poll_list')


class ChoiceDelete(DeleteView):
    model = Choice
    template_name = 'choice_delete.html'
    context_object_name = 'choice'
    success_url = reverse_lazy('poll_list')

