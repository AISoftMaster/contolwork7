from django.urls import path
from .views import PollListView, PollDetailView

urlpatterns = [
    path('', PollListView.as_view(), name='poll_list'),
    path('poll/<int:pk>/', PollDetailView.as_view(), name='poll_detail')
]
