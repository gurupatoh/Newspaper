from django.urls import path
from .views import (
    JobListView,
    JobUpdateView,
    JobDetailView,
    JobDeleteView,  # new
    JobCreateView,
    ClientListView
)

urlpatterns = [
    # path('category/', JobListView.as_view, name='job_list'),
    # path('category/P<pk>/', JobDetailView.as_view, name='job_detail'),
    path('<int:pk>/edit/',
         JobUpdateView.as_view(), name='job_edit'),  # new
    path('details/', JobDetailView.as_view(), name='job_detail'),  # new
    path('<int:pk>/delete/',
         JobDeleteView.as_view(), name='job_delete'),  # new
    path('new/', JobCreateView.as_view(), name='job_new'),  # new
    path('list/', JobListView.as_view(), name='job_list'),
    path('client/', ClientListView.as_view(), name='client_listings'),

]
