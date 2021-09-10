from django.urls import path
from .views import SignUpView

urlpatterns = [
    path('registro/', SignUpView.as_view(), name="signup"),
    # path('perfil/', ProfileUpdate.as_view(), name="profile"),
    # path('perfil/email/', EmailUpdate.as_view(), name="profile_email"),
    # path('login-register/', SignUpRegisterView.as_view(), name="signup_register"),
]