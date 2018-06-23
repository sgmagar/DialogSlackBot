from django.urls import path

from dialogbot.views import IndexView, OauthCallbackView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('oauth-callback/', OauthCallbackView.as_view(), name='oauth_callback'),
]
