from rest_framework import serializers

from comment.models import Comment
from user_info.serializers import UserDescSerializer

# 子类
class CommentChildrenSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='comment-detail')
    author = UserDescSerializer(read_only=True)

    class Meta:
        model = Comment
        exclude = [
            'parent',
            'article'
        ]

# 父类
class CommentSerializer(serializers.ModelSerializer):
    # url超链接
    url = serializers.HyperlinkedIdentityField(view_name='comment-detail')
    # 嵌套序列化器
    author = UserDescSerializer(read_only=True)

    # 多级评论，超链接字段HyperlinkedRelatedField
    # HyperlinkedRelatedField用于外键关系，HyperlinkedRelatedField用于模型自身
    article = serializers.HyperlinkedRelatedField(view_name='article-detail', read_only=True)
    article_id = serializers.IntegerField(write_only=True, allow_null=False, required=True)

    parent = CommentChildrenSerializer(read_only=True) # 父评论
    parent_id = serializers.IntegerField(write_only=True, allow_null=True, required=False)

    # 覆写update，使得父评论不能被修改
    def update(self, instance, validated_data):
        # 更新时剔除 parent 字段
        validated_data.pop('parent_id', None) # 更新评论时忽略掉parent_id参数
        return super().update(instance, validated_data)

    class Meta:
        model = Comment
        fields = '__all__'
        extra_kwargs = {'created': {'read_only': True}}