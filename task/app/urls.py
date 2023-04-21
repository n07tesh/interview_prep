from django.urls import path,include
from rest_framework.routers import DefaultRouter
from app.views import Task
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()

router.register(r'task',Task,basename='task')
# urlpatterns = router.urls
urlpatterns = [
     path('', include(router.urls)),
     path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]