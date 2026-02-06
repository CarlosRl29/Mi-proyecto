from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, AdministrationViewSet, MemberViewSet, ExerciseViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'administrations', AdministrationViewSet)
router.register(r'members', MemberViewSet)
router.register(r'exercises', ExerciseViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
