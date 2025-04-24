from django.contrib import admin
from django.http import HttpResponse, JsonResponse
from django.urls import include, path
import time

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django_prometheus.urls')),
    path("health/", lambda request: (time.sleep(10), JsonResponse({ "status": "OK" }, status=200))[1], name="health"),
]
