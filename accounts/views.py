from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.views import APIView
from accounts.models import Profile
from accounts.serializers import ProfileSerializer, RegisterSerializer, SigninSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from django.urls import reverse
from django.contrib import messages
from accounts.forms import ProfileForm

def home(request):
    return render(request, 'home.html')

class ProfilesListAPIView(LoginRequiredMixin,APIView):
    serializer_class = ProfileSerializer
    

    def get_queryset(self):
        return Profile.objects.order_by('pk')  # Always fetch fresh data

    @method_decorator(cache_page(60 * 5))  # Cache the response for 5 minutes
    def get(self, request):
        profiles = self.get_queryset()  # Use get_queryset() to fetch profiles
        serializer = self.serializer_class(profiles, many=True)  # Serialize the queryset
        return Response(serializer.data, status=status.HTTP_200_OK)  # Return a DRF Response

class ProfileDetailAPIView(LoginRequiredMixin, APIView):
    serializer_class = ProfileSerializer

    def get(self, request, pk):
        profile = get_object_or_404(Profile, pk=pk)  # Fetch the profile by pk
        serializer = self.serializer_class(profile)  # Serialize the profile
        return Response(serializer.data, status=status.HTTP_200_OK)  # Return a DRF Response


class ProfilesUpdateAPIView(APIView):
    model = Profile
    form_class = ProfileForm

    @method_decorator(login_required)
    def get(self, request, pk):
        profile = get_object_or_404(self.model, pk=pk)
        form = self.form_class(instance=profile)
        return render(request, 'accounts/profile_update.html', {'form': form, 'profile': profile})
    
    @method_decorator(login_required)
    def post(self, request, pk):
        profile = get_object_or_404(self.model, pk=pk)
        form = self.form_class(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect(reverse('profiles_list'))  
        return render(request, 'accounts/profile_update.html', {'form': form, 'profile': profile})

class RegisterCreateAPIView(generics.CreateAPIView):
    
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    



def register_page(request):
    return render(request, 'accounts/register.html')


class SignInAPIView(APIView):
   
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            refresh = RefreshToken.for_user(user) 
            access = str(refresh.access_token)
            print(access)
            return Response({"refresh": str(refresh), "access": access},status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
    def success(request):
        return HttpResponse('Login sucess')
        
def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user) 
            access = str(refresh.access_token)
            print(access)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'accounts/sign_in.html', {'title': 'Login'})

def logout_view(request):
    logout(request)
    return redirect('login')

