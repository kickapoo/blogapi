from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

API_TITLE = 'Simple Blog API'
API_DESCRIPTION = 'A simple Blog API to enchant my DRF learing curve'

schema_view = get_schema_view(title=API_TITLE)
swagger_view = get_swagger_view(title=API_TITLE)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),
    path('api-auth/', include('rest_framework.urls')), # Add Log In in Browsable API
    path('api/v1/rest-auth/', include('rest_auth.urls')), # Login/Logout/Password Reset/Password Reset Confirm
    path('api/v1/rest-auth/registration', include('rest_auth.registration.urls')), # Registration Urls
    path('api/docs', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    path('api/schema', schema_view),
    path('api/swagger', swagger_view)
]
