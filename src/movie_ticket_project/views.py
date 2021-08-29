from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view


@api_view(http_method_names=['POST'])
def signup(request):
    try:
        username = request.data["username"]
        password = request.data["password"]
        user = User.objects.create_user(username=username, password=password)
        return JsonResponse({"token": user.auth_token.key, "id": user.pk})
    except Exception as ex:
        print(ex)
        return JsonResponse({"error": "error creating user"}, status=500)


@api_view(http_method_names=['POST'])
def get_auth_token(request):
    try:
        data = request.data
        user = authenticate(username=data['username'],
                            password=data['password'])
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return JsonResponse({
                'token': token.key,
                'user_id': user.pk,
            })
        else:
            return JsonResponse({"error": "no such user found"})
    except Exception as ex:
        print(ex)
        return JsonResponse({"error": "internal server error"}, status=500)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
