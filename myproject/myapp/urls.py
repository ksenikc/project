from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include, reverse
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('newproduct/', set_orders, name='newproduct'),
    path('application/', applic, name='application'),
    path('application/<int:pk>/delete', OrdersDeleteView.as_view(), name='app_delete'),
    path('application/<int:pk>/decision', OrdersUpdateView.as_view(), name='app_decision'),
    path('application/<int:pk>/deviation', OrdersUpdatesView.as_view(), name='app_deviation'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
