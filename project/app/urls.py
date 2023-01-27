from django.urls import path
from .views import PostsList, PostDetail, PostSearch, PostCreate, PostUpdate, PostDelete

urlpatterns = [
   path('', PostsList.as_view(), name='post_list'),
   path('search/', PostSearch.as_view(), name='post_search'),
   path('<int:pk>', PostDetail.as_view(), name='post_details'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/edit', PostUpdate.as_view(), name='post_update'),
   path('<int:pk>/delete', PostDelete.as_view(), name='post_delete'),

   path('accounts/login/', PostDelete.as_view(), name='login'),
   path('accounts/logout/', PostDelete.as_view(), name='logout'),
   path('accounts/password_change/', PostDelete.as_view(), name='password_change'),
   path('accounts/password_change/done/', PostDelete.as_view(), name='password_change_done'),
   path('accounts/password_reset/', PostDelete.as_view(), name='password_reset'),
   path('accounts/password_reset/done/', PostDelete.as_view(), name='password_reset_done'),
   path('accounts/reset///', PostDelete.as_view(), name='password_reset_confirm'),
   path('accounts/reset/done/', PostDelete.as_view(), name='password_reset_complete'),
]
