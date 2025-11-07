from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")

class CustomAuthenticationForm(AuthenticationForm):
    pass

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "email")

class CustomPasswordChangeForm(PasswordChangeForm):
    pass