from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateMessage,MessageDetails,UserView,UserDetailsView,CreateUser
from rest_framework.authtoken.views import obtain_auth_token
from django.views.decorators.csrf import csrf_exempt

urlpatterns = {
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')), 
    url(r'^messages/$', CreateMessage.as_view(), name="create"),
    url(r'^signup/$',CreateUser.as_view(),name='create_user'),
    url(r'^messages/(?P<pk>[0-9]+)/$', MessageDetails.as_view(), name="details"),
    url(r'^users/$', UserView.as_view(), name="users"),
    url(r'users/(?P<pk>[0-9]+)/$', UserDetailsView.as_view(), name="user_details"),
    url(r'^get-token/', obtain_auth_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)