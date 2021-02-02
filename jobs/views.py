from django.contrib.auth.mixins import LoginRequiredMixin  # mixin
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404


from .models import Job


class JobListView(LoginRequiredMixin, ListView):
    model = Job


# def category_list(request):
#     categories = Category.objects.all()
    # print(type(Categories))
    # print(categories)

    # return render(request, 'job_list.html', {
    # categories: categories})

    template_name = 'job_list.html'
    login_url = 'login'  # new


class ClientListView(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'client_listings.html'
    login_url = 'login'  # new


class JobDetailView(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'job_detail.html'
    login_url = 'login'  # new


# def category_detail(request, pk):
#     category = get_object_or_404(Category, pk=pk)
#     return render(request, 'job_detail.html', {'category': category})


class JobUpdateView(LoginRequiredMixin, UpdateView):
    model = Job
    fields = ('title', 'body')

    template_name = 'job_edit.html'
    login_url = 'login'  # new

    def dispatch(self, request, *args, **kwargs):  # new
        obj = self.get_object()

        if obj.client != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class JobDeleteView(LoginRequiredMixin, DeleteView):
    model = Job
    template_name = 'job_delete.html'
    success_url = reverse_lazy('job_list')
    login_url = 'login'  # new

    def dispatch(self, request, *args, **kwargs):  # new
        obj = self.get_object()
        if obj.client != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class JobCreateView(LoginRequiredMixin, CreateView):
    model = Job

    fields = ('title', 'location', 'body')
    template_name = 'job_new.html'

    login_url = 'login'  # new


def form_valid(self, form):
    form.instance.client = self.request.user
    return super().form_valid(form)
