from django.contrib import admin

# Register your models here.
# 别忘了导入Article等
from .models import Article, Category, Tag, Avatar

# 注册Article到admin中
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Avatar)