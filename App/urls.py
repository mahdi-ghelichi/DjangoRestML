from App.views import Train
# from rest_framework_jwt.views import obtain_jwt_token
# from rest_framework_jwt.views import refresh_jwt_token
# from rest_framework_jwt.views import verify_jwt_token
from django.conf.urls import url

app_name = 'App'


urlpatterns = [
    # url(r'^generate-token/', obtain_jwt_token),
    # url(r'^generate-token-refresh/', refresh_jwt_token),
    # url(r'^generate-token-verify/', verify_jwt_token),
    url(r'^train/$', Train.as_view(), name="train"),
    # url(r'^predict/$', predict.as_view(), name="predict"),
]
