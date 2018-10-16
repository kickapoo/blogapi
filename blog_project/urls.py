from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Simple Blog API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),
    path('api-auth/', include('rest_framework.urls')), # Add Log In in Browsable API
    path('api/v1/rest-auth/', include('rest_auth.urls')), # Login/Logout/Password Reset/Password Reset Confirm
    path('api/v1/rest-auth/registration', include('rest_auth.registration.urls')), # Registration Urls
    path('api/schema/', schema_view)
]
