from django.urls import path
from .views import PollListView, PollDetailView, PollCreate, PollUpdate, PollDelete, ChoiceDelete, ChoiceCreate

urlpatterns = [
    path('', PollListView.as_view(), name='poll_list'),
    path('<int:pk>/', PollDetailView.as_view(), name='poll_detail'),
    path('create/', PollCreate.as_view(), name='poll_create'),
    path('<int:pk>/update/', PollUpdate.as_view(), name='poll_update'),
    path('<int:pk>/delete/', PollDelete.as_view(), name='poll_delete'),
    path('<int:pk>/choice/<int:pk2>/delete/', ChoiceDelete.as_view(), name='choice_delete'),
    path('<int:pk>/choice/create/', ChoiceCreate.as_view(), name='choice_create'),
]
