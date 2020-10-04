from django.urls import path
from .views import (
    JobListView,
    JobUpdateView,
    JobDetailView,
    JobDeleteView,  # new
    JobCreateView,
)

urlpatterns = [
    path('<int:pk>/edit/',
         JobUpdateView.as_view(), name='job_edit'),  # new
    path('<int:pk>/',
         JobDetailView.as_view(), name='job_detail'),  # new
    path('<int:pk>/delete/',
         JobDeleteView.as_view(), name='job_delete'),  # new
    path('new/', JobCreateView.as_view(), name='job_new'),  # new
    path('', JobListView.as_view(), name='job_list'),
]
