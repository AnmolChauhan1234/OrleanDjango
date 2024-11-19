from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import healthcare_dashboard

urlpatterns = [
    path('',healthcare_dashboard,name='healthcare_dashboard')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)