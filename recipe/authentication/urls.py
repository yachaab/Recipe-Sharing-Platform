from django.urls import re_path, include

urlpatterns = [
    re_path(r'', include('rest_registration.api.urls'), name='accounts'),
]