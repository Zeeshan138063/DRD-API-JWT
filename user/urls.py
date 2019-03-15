from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

from user.views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns =[

    # url(r'^auth/', include('rest_auth.urls')),
    url('login/', obtain_jwt_token, name="auth-login"),
    # path('password/reset/', PasswordResetView.as_view(),
    #      name='rest_password_reset'),
    # path('password/reset/confirm/', PasswordResetConfirmView.as_view(),
    #      name='rest_password_reset_confirm'),
    # path('password/change/', PasswordChangeView.as_view(),
    #      name='rest_password_change'),

]
# urlpatterns+=   url(r'^', include(router.urls)),
urlpatterns+=   router.urls