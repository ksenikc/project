from django.http import Http404
from .forms import NewApplicationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Stat, Application
from .filters import OrdersFilter
from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.http import JsonResponse


def home(request):
    # Получаем 4 последние решенные заявки
    posts = Application.objects.filter(stat='2').order_by('-date')[:4]
    solved_count = Application.objects.filter(stat='2').count()

    return render(request, 'myapp/index.html', {
        'posts': posts,
        'solved_count': solved_count
    })


def get_solved_count(request):
    count = Application.objects.filter(stat='solved').count()
    return JsonResponse({'count': count})


def set_orders(request):
    if request.method == 'POST':
        form = NewApplicationForm(request.POST, request.FILES)
        form.instance.owner = request.user
        print('----------')
        print(request)
        print(settings.MEDIA_URL)
        print(settings.MEDIA_ROOT)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            raise Http404
    else:
        form = NewApplicationForm()
    return render(request, 'myapp/new_application.html', {'form': form})


def applic(request):
    filter = None
    try:
        if request.user.is_superuser:
            filter = OrdersFilter(request.GET, queryset=Application.objects.order_by('-date'))
        else:
            filter = OrdersFilter(request.GET, queryset=Application.objects.filter(owner=request.user).order_by('id'))
    except Exception as e:
        orders = None
    return render(request, 'myapp/application.html', {'filter': filter})


class OrdersDeleteView(DeleteView):
    model = Application
    template_name = 'myapp/application_delete.html'
    success_url = reverse_lazy('home')


class OrdersUpdateView(UpdateView):
    model = Application
    fields = ['image_after', 'stat']
    template_name = 'myapp/Decision_application.html'
    success_url = reverse_lazy('application')


class OrdersUpdatesView(UpdateView):
    model = Application
    fields = ['rejection_reason', 'stat']
    template_name = 'myapp/Deviation_application.html'
    success_url = reverse_lazy('application')
