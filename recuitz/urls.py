from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, QuestionViewSet, ResultViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('questions', QuestionViewSet)
router.register('results', ResultViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
