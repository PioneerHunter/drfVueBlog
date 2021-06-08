# 文章视图
from article.models import Article # 文章
from article.models import Category # 文章分类
from article.models import Tag # 文章标签
from article.models import Avatar # 文章标题图

from article.permissions import IsAdminUserOrReadOnly # 权限控制类，管理员、用户

from rest_framework import viewsets # 视图集

# 序列器
from article.serializers import ArticleSerializer # Article用到的集成序列化器
from article.serializers import ArticleDetailSerializer # 文章详情序列化器
# Category用到的集成序列化器
from article.serializers import CategorySerializer, CategoryDetailSerializer
from article.serializers import TagSerializer # 文章标签序列化器
from article.serializers import AvatarSerializer # 文章标题图序列化器

from rest_framework import filters # 过滤器

# 文章标题、详情 类，列表、详情逻辑已集成，并提供了默认的增删改查的实现
class ArticleViewSet(viewsets.ModelViewSet): # 基础逻辑封装在ModelViewSet中
    """博文视图集"""
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    # 过滤文章标题，模糊匹配
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
    # markdown    
    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleSerializer
        else:
            return ArticleDetailSerializer

# 文章分类 类
class CategoryViewSet(viewsets.ModelViewSet):
    """分类视图集"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = None

    def get_serializer_class(self):
        if self.action == 'list':
            return CategorySerializer
        else:
            return CategoryDetailSerializer

# 文章标签 类
class TagViewSet(viewsets.ModelViewSet):
    """标签视图集"""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = None

# 文章标题图 类
class AvatarViewSet(viewsets.ModelViewSet):
    """标题图视图集"""
    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = None