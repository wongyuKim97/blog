from django.contrib import admin
from django.urls import path, include
import blog1.views
import portfolio.views
import accounts.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog1.views.home, name = "home"),
    path('detail/', include('blog1.urls')),
    path('accounts/', include('accounts.urls')),
    path('portfolio/', portfolio.views.portfolio, name = "portfolio"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)