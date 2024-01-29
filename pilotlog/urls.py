
from django.contrib import admin
from django.urls import (
    path,
    include,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('user.urls')),
    path('api/data/', include('pilot_data_api.urls')),
]
