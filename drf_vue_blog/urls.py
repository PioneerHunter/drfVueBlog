from django.contrib import admin
from django.urls import path
from django.urls import include # 添加drf视图

from article import views
from user_info.views import UserViewSet # 用户视图集
from comment.views import CommentViewSet # 评论视图集

# 引入Router类（路由）
# Router可以提供一个接口导航
from rest_framework.routers import DefaultRouter

from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# 路由
router = DefaultRouter()
router.register(r'article', views.ArticleViewSet) # Article视图集
router.register(r'category', views.CategoryViewSet) # Category视图集
router.register(r'tag', views.TagViewSet) # Tag视图集
router.register(r'avatar', views.AvatarViewSet) # Avatar视图集
router.register(r'comment', CommentViewSet) # 评论视图集
router.register(r'user', UserViewSet) # 用户视图集

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')), # 添加drf视图
    # drf 自动注册路由
    path('api/', include(router.urls)),
    # JWT验证
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# 把媒体文件的路由注册了
if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)