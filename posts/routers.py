from rest_framework.routers import DefaultRouter
from .viewsets import PostViewSet, LoginViewSet

router = DefaultRouter()

router.register("post-view-set", PostViewSet)
router.register("login-view-set", LoginViewSet, base_name="login-view-set")