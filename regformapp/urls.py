from rest_framework.routers import DefaultRouter
from .views import StudentView, StudentMark
from django.urls import path, include

""" 
Model-view urls 
"""

router = DefaultRouter()
router.register('form', StudentView)
router.register('mark', StudentMark)
urlpatterns = [
    path('api/', include(router.urls))
]
