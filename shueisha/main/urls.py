from django.urls import path
from . import views
from .views import UpdatePostView, UpdateReviewView

urlpatterns = [
    
#    blogs
    path("", views.blogs, name="blogs"),
    path("blog/<str:slug>/", views.blogs_comments, name="blogs_comments"),
    path("add_blogs/", views.add_blogs, name="add_blogs"),
    path("edit_blog_post/<str:slug>/", UpdatePostView.as_view(), name="edit_blog_post"),
    path("delete_blog_post/<str:slug>/", views.Delete_Blog_Post, name="delete_blog_post"),

#  reviews
    path("review/", views.reviews, name="reviews"),
    path("review/<str:slug>/", views.reviews_comments, name="reviews_comments"),
    path("add_reviews/", views.add_reviews, name="add_reviews"),
    path("edit_review_post/<str:slug>/", UpdateReviewView.as_view(), name="edit_reviews_post"),
    path("delete_review_post/<str:slug>/", views.Delete_Review_Post, name="delete_review_post"),
    
#   search    
    path("search/", views.search, name="search"),
    
#    perfil
    path("profile/", views.Profile, name="profile"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("user_profile/<int:myid>/", views.user_profile, name="user_profile"),
    
#   autenticación de usuario
    path("register/", views.Register, name="register"),
    path("login/", views.Login, name="login"),
    path("logout/", views.Logout, name="logout"),
]