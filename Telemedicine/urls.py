from django.conf.urls.static import static
from django.urls import path, include

from Telemedicine import settings

urlpatterns = [
                  path('', include('telemedicineApp.urls')),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
