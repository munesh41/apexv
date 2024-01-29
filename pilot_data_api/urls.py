
from django.urls import path

from pilot_data_api import views

app_name = 'pilot_data_api'

urlpatterns = [
    path('import/', views.ImportDataView.as_view(), name='import_data'),
]