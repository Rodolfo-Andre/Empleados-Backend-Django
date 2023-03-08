from django.urls import path
from rest_framework.routers import DefaultRouter
from .api import EmployeeView

router = DefaultRouter()
router.register(r'', EmployeeView)

urlpatterns = router.urls
