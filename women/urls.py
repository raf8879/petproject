from django.urls import path, re_path, register_converter
from . import views, convertors
from django.views.decorators.cache import cache_page


register_converter(convertors.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.WomenHome.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('addpage/', views.Addpage.as_view(), name='add_page'),
    path('contact/', views.ContactFromView.as_view(), name='contact'),
    path('login', views.login, name='login'),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', views.WomenCategory.as_view(), name='category'),
    path('tag/<slug:tag_slug>/', views.TagPostList.as_view(), name='tag'),
    path('edit/<slug:slug>/', views.UpdatePage.as_view(), name='edit_page'),
    path('delete/<int:pk>/', views.DeletePage.as_view(), name='delete_page'),
]


