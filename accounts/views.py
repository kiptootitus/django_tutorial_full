from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.views import APIView
from accounts.models import Profile
from accounts.serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate



def home(request):
    return render(request, 'accounts/home.html')

class ProfilesListView(View):
    model = None  # Placeholder to be defined in subclasses
    
    def get(self, request):
        if not self.model:
            return HttpResponse("Model not defined.", status=500)
        
        modelname = self.model._meta.verbose_name_plural.lower()
        profiles = self.model.objects.all()
        context = {modelname: profiles}
        
        return render(request, f'accounts/{modelname}_list.html', context)

class AccountsListView(ProfilesListView):
    model = Profile


class RegisterCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
# New Template View for serving the HTML form
def register_page(request):
    return render(request, 'accounts/register.html')


class SignInAPIView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # refresh = RefreshToken(refresh)
            refresh = RefreshToken.for_user(user)  # Generate a new Refresh Token
            access = str(refresh.access_token)
            return Response({"refresh": str(refresh), "access": access},status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)