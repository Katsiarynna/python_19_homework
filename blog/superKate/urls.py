from django.urls import path, include
from .views import hello, page_view, PageListView, PageCreateView, PageDetailView, PageUpdateView, PageDeleteView
from .models import Page
from .views import review_view, ReviewListView, ReviewCreateView, ReviewDetailView, ReviewUpdateView, ReviewDeleteView


urlpatterns = [
    path('hello/', hello, name="hello"),
    path('all_pages_func/', page_view, name="all_pages_func"),
    path('all_review_func/', review_view, name="all_review_func"),
    path('all_pages_class/', PageListView.as_view(), name="all_pages_class"),
    path('all_review_class/', ReviewListView.as_view(), name="all_review_class"),
    path('create_page/', PageCreateView.as_view(), name="create_page"),
    path('create_review/', ReviewCreateView.as_view(), name="create_review"),
    path('detail_page/<int:pk>', PageDetailView.as_view(), name="detail_page"),
    path('detail_review/<int:pk>', ReviewDetailView.as_view(), name="detail_review"),
    path('update_page/<int:pk>', PageUpdateView.as_view(), name="update_page"),
    path('update_review/<int:pk>', ReviewUpdateView.as_view(), name="update_review"),
    path('delete_page/<int:pk>', PageDeleteView.as_view(), name="delete_page"),
    path('delete_review/<int:pk>', ReviewDeleteView.as_view(), name="delete_review")
]


