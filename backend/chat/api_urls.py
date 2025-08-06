from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ChatViewSet, AgentViewSet

#创建路由器实例并注册视图集
router = DefaultRouter()
router.register(r'chats', ChatViewSet)
router.register(r'agents', AgentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]