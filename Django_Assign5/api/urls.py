from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from .views import CreateTransaction, CreateCategory, TransactionDetailsView, CategoryDetailsView, UserView,TransactionsCategoryView, UserDetailsView, ViewCategory, UserTransactionsView

urlpatterns = {
    url(r'^transactions/$', CreateTransaction.as_view(), name="create"),
    url(r'^transactions/(?P<pk>[0-9]+)/$',
        TransactionDetailsView.as_view(), name="details"),
    url(r'^categories/$', ViewCategory.as_view(), name="create"),
    url(r'^categories/(?P<category_id>[0-9]+)/$',
        CategoryDetailsView.as_view(), name="details"),
    url(r'^users/$', UserView.as_view(), name="users"),
    url(r'users/(?P<user_id>[0-9]+)/$', UserDetailsView.as_view(), name="user_details"),
    url(r'users/(?P<user_id>[0-9]+)/transactions$', UserTransactionsView.as_view(), name="user_transactions"),
    url(r'categories/(?P<category_id>[0-9]+)/transactions$', TransactionsCategoryView.as_view(), name="transactions_category"),
    url(r'^auth/', include('rest_framework.urls',namespace='rest_framework')),
    url(r'^get_token/', obtain_auth_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)