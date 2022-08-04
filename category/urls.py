from django.urls import path
from .views import *

app_name = "category"

urlpatterns = [
    path('', tool_in_category, name='tool_all'),
    path('upload/', upload_csv, name='upload_csv'),
    path('upload/ajax_method/', ajax_method, name='ajax_method')
]