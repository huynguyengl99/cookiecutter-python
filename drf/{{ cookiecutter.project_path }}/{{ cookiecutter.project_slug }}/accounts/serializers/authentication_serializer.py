from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from dj_rest_auth.serializers import LoginSerializer as BaseLoginSerializer


class LoginSerializer(BaseLoginSerializer):
    username = None
    email = serializers.EmailField(required=True, allow_blank=False)

    @staticmethod
    def validate_email_verification_status(user, email=None):
        from allauth.account import app_settings as allauth_account_settings

        if (
            allauth_account_settings.EMAIL_VERIFICATION
            == allauth_account_settings.EmailVerificationMethod.MANDATORY
            and not user.emailaddress_set.filter(
                email=user.email, verified=True
            ).exists()
            and not user.is_admin
        ):
            raise serializers.ValidationError(_("E-mail is not verified."))


class LogoutSerializer(serializers.Serializer):
    token = serializers.CharField(write_only=True, required=False)
    detail = serializers.CharField(read_only=True)
