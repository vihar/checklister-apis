import uuid
import json

from django.contrib.auth.models import User
from django.views.generic import View

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from allauth.socialaccount.providers.facebook.views import (
    FacebookOAuth2Adapter
)

from rest_framework_jwt.settings import api_settings

from allauth.utils import generate_unique_username
from .users import Profile, SocialProvider
from rest_auth.registration.views import SocialConnectView

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class SocialLoginView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(SocialLoginView, self).dispatch(request, *args, **kwargs)

    def post(self, request):
        """
        Generate JWT Token
        """
        payload = json.loads(request.body)

        # TODO: Handle these later
        email = payload['email']
        extra = payload['extra']
        provider = payload['provider']

        try:
            user = User.objects.get(email=email)
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)

            # Profile Verification
            has_details = self.user_profile_verification(user)

            # user_data being passed into Response
            data = self.user_data(user, token, has_details)

            # Update Social Provider Details
            self.social_provider_auth(user, provider, extra)
            return JsonResponse(data)

        except User.DoesNotExist:
            username = generate_unique_username([email])
            pw = str(uuid.uuid4())
            user = User.objects.create_user(username, email=email, password=pw)
            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)

            # Profile Verification
            has_details = self.user_profile_verification(user)

            # user_data being passed into Response
            data = self.user_data(user, token, has_details)

            # Update Social Provider Details
            self.social_provider_auth(user, provider, extra)
            return JsonResponse(data)

    def user_data(self, user, token, has_details):
        user_data = {}
        user_data['user_email'] = user.email
        user_data['user_name'] = user.username
        user_data['user_is_staff'] = user.is_staff
        user_data['user_is_active'] = user.is_active
        user_data['user_is_superuser'] = user.is_superuser
        user_data['token'] = token
        user_data['has_details'] = has_details
        return user_data

    def social_provider_auth(self, user, provider, extra):
        provider, created = SocialProvider.objects.get_or_create(
            user=user, provider=provider)
        provider.extra = extra
        provider.save()
        return

    def user_profile_verification(self, user):
        profile, created = Profile.objects.get_or_create(user=user)
        has_details = profile.has_details()
        return has_details


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class FacebookConnect(SocialConnectView):
    adapter_class = FacebookOAuth2Adapter
