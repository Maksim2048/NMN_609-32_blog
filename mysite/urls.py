from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from mysite import views
from articles import views as articles_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', articles_views.article_list, name='homepage'),
    path('about/', views.about, name='about'),
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)