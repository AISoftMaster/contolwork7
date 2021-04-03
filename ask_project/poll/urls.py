from django.urls import path
from .views import PollListView, PollDetailView, PollCreate

urlpatterns = [
    path('', PollListView.as_view(), name='poll_list'),
    path('<int:pk>/', PollDetailView.as_view(), name='poll_detail'),
    path('create/', PollCreate.as_view(), name='poll_create'),
]
