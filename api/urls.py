from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookViewSet

router= DefaultRouter()

router.register(r'Book', BookViewSet)

urlpatterns =[
    path('api/', include(router.urls)),
    path('api-token-auth/',obtain_auth_token, name='api-token-auth')
]