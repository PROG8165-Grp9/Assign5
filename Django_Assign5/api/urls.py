from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth import views as auth_views
from rest_framework_jwt.views import obtain_jwt_token
from .views import (CreateTransaction,
                    CreateCategory,
                    TransactionDetailsView,
                    CategoryDetailsView,
                    UserView,
                    TransactionsCategoryView,
                    UserDetailsView,
                    ViewCategory,
                    UserCreateView,
                    UserTransactionsView,
                    UserLoginView)

urlpatterns = {
    url(r'^$', auth_views.login, {'template_name': 'API/LogIn.html'}, name='login', ),
    url(r'^transactions/$', CreateTransaction.as_view(), name="create-transaction"),
    url(r'^transactions/(?P<pk>[0-9]+)/$',
        TransactionDetailsView.as_view(), name="transaction-details"),
    url(r'^categories/$', ViewCategory.as_view(), name="category"),
    url(r'^categories/(?P<category_id>[0-9]+)/$',
        CategoryDetailsView.as_view(), name="category-details"),
    url(r'^users/$', UserView.as_view(), name="users"),
    url(r'users/(?P<user_id>[0-9]+)/$', UserDetailsView.as_view(), name="user0details"),
    url(r'users/(?P<user_id>[0-9]+)/transactions$', UserTransactionsView.as_view(), name="user-transactions"),
    url(r'categories/(?P<category_id>[0-9]+)/transactions$', TransactionsCategoryView.as_view(), name="transactions-category"),
    url(r'^register', UserCreateView.as_view(), name="create-user"),
    url(r'^login', UserLoginView.as_view(), name="login"),
    url(r'^auth/token/', obtain_jwt_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)