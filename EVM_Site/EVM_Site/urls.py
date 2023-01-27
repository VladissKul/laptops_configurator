from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from EVM_Site import settings
from laptop_shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('gamer_laptop/', views.gamer_laptop, name='gamer_laptop'),
    path('os_laptop/', views.os_laptop, name='os_laptop'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
