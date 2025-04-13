from django.urls import path
# from .views import RequestResetView, VerifyOTPView, ResetPasswordView
from .views import TestAuthenticatedView, LoginView, CreateEmployeeView
from rest_framework.authtoken.views import obtain_auth_token
 
urlpatterns = [
    # path('auth/request-reset/', RequestResetView.as_view()),
    # path('auth/verify-otp/', VerifyOTPView.as_view()),
    # path('auth/reset-password/', ResetPasswordView.as_view()),
    path('auth/test-authenticated/', TestAuthenticatedView.as_view()),
    path('auth/login/', LoginView.as_view()),  # Login endpoint
    path('auth/create-employee/', CreateEmployeeView.as_view()), # Create employee endpoint
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Token authentication endpoint
]
