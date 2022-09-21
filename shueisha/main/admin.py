from django.contrib import admin
from .models import *


admin.site.register(BlogPost)
admin.site.register(ReviewPost)
admin.site.register(CommentReview)
admin.site.register(CommentBlog)
admin.site.register(Profile)
