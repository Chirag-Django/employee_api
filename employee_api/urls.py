from django.urls import path,include
from rest_framework import routers
from .views import EmployeeCRUDAPIView

router = routers.DefaultRouter()
router.register('',EmployeeCRUDAPIView,basename='emp-api')

urlpatterns = [
    path('emp-api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]