from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

#routes 
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    #ex http://localhost:8000/admin
    path('admin/', admin.site.urls),
    #ex http://localhost:8000/api 
    path('api/', include('testb.api.urls'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
