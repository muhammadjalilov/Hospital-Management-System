from rest_framework import views, status
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter
import jwt
from django.conf import settings
from django.contrib.auth import get_user_model

from apps.shared.serializers import EmailVerificationSerializer

User = get_user_model()


class VerifyEmail(views.APIView):
    serializer_class = EmailVerificationSerializer

    @extend_schema(
        description="Verify user email using the token.",
        parameters=[
            OpenApiParameter(
                name="token",
                type=str,
                location=OpenApiParameter.QUERY,
                required=True,
                description="JWT token for email verification"
            )
        ],
    )
    def get(self, request):
        # Fetch token from query parameters (URL)
        token = request.GET.get('token')
        print(f"Token from query: {token}")

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user = User.objects.get(id=payload['user_id'])
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError:
            return Response({'error': 'Activation link expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
