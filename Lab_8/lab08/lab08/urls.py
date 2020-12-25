from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    path('catalog/', include('catalog.urls')),
    path('admin/', admin.site.urls),
]
