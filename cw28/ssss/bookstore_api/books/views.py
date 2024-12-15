import random
from django_otp.oath import totp
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken 
from .models import User
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.permissions import AllowAny



class GenerateOTPView(APIView):
    # throttle_scope = 'otp_generate'
    # throttle_classes = [ScopedRateThrottle]
    permission_classes = [AllowAny]
    def post(self, request):
        
        phone_number = request.data.get('phone_number')
        user, created = User.objects.get_or_create(phone_number=phone_number)
        otp = random.randint(100000, 999999) # Replace with a real OTP generator in production
        # Send OTP via SMS (pseudo-code)
        print(f"OTP for {phone_number}: {otp}") 
        request.session[f'otp_{phone_number}'] = otp 
        return Response({"message": "OTP sent to phone number."})


class VerifyOTPView(APIView):
    # throttle_scope = 'otp_verify'
    # throttle_classes = [ScopedRateThrottle]
    permission_classes = [AllowAny]

    def post(self, request):
        phone_number = request.data.get('phone_number')
        otp = request.data.get('otp')
        saved_otp = request.session.get(f'otp_{phone_number}') 
        if str(otp) == str(saved_otp):
            user = User.objects.get(phone_number=phone_number) 
            refresh = RefreshToken.for_user(user)
            return Response({"access": str(refresh.access_token),"refresh": str(refresh)})
        return Response({"error": "Invalid OTP."}, status=400)


