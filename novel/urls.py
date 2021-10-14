from django.urls import path
from .import views

app_name = 'novel'

urlpatterns = [
    path('', views.Top.as_view(), name='novel_top'),
    path('list/', views.StoryList.as_view(), name='story_list'),
    path('detail/<int:pk>/', views.StoryDetail.as_view(), name='story_detail'),
    path('comment/<int:pk>/', views.CommentCreate.as_view(), name='comment_create'),
    path('create/', views.StoryCreate.as_view(), name='story_create'),
    path('category/create/', views.CategoryCreate.as_view(), name='category_create'),
    path('tag/create/', views.TagCreate.as_view(), name='tag_create'),
    path('update/<int:pk>', views.StoryUpdate.as_view(), name='story_update'),
    path('category/<int:pk>/', views.StoryCategoryList.as_view(), name="story_category_list"),
    path('tag/<int:pk>/', views.StoryTagList.as_view(), name="story_tag_list"),
    path('terms/', views.Terms.as_view(), name="was_terms"),


]
