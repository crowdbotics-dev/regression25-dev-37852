from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    AddeddataViewSet,
    HimanshutestViewSet,
    TestViewSet,
    UsertestViewSet,
)

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("test", TestViewSet)
router.register("himanshutest", HimanshutestViewSet)
router.register("usertest", UsertestViewSet)
router.register("addeddata", AddeddataViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
