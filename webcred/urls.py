from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from webcred import views

urlpatterns = [
    path('', views.home, name='home'),
    path('assess/', views.assess, name='assess')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
