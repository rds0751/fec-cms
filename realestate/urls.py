from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
path('', include('pages.urls')),
path('listings/', include('listings.urls')),
path('accounts/', include('accounts.urls')),
path('contact/', include('marketing.urls')),
path('admin/', admin.site.urls),
path('reviews/', include('reviews.urls')),

path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
path('ckeditor/', include('ckeditor_uploader.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)