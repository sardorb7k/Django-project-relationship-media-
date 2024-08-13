from django.contrib import admin
from django.urls import path
from blog.views import index, AboutPage, UsersPage
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('about/<int:id>/', AboutPage, name='about'),
    path('users/', UsersPage, name='users'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
