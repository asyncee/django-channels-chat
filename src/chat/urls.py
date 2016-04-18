from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


from chat_engine import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.chat, name='chat'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
