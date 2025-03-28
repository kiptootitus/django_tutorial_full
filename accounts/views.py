from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.views import APIView
from accounts.models import Profile
from accounts.serializers import RegisterSerializer, SigninSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.views.decorators.http import require_POST
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.contrib import messages
from accounts.forms import ProfileForm  # Assuming you have a ProfileForm for the Profile model

def home(request):
    return render(request, 'home.html')

class ProfilesListAPIView(LoginRequiredMixin,APIView):
    model = None  # Placeholder to be defined in subclasses
    
    def get(self, request):
        if not self.model:
            return HttpResponse("Model not defined.", status=500)
        
        modelname = self.model._meta.verbose_name_plural.lower()
        profiles = self.model.objects.all()
        context = {modelname: profiles}
        
        return render(request, f'accounts/{modelname}_list.html', context)

class AccountsListAPIView(ProfilesListAPIView):
    model = Profile



class ProfilesUpdateAPIView(LoginRequiredMixin, APIView):
    model = Profile
    form_class = ProfileForm

    def get(self, request, pk):
        profile = get_object_or_404(self.model, pk=pk)
        form = self.form_class(instance=profile)
        return render(request, 'accounts/profile_update.html', {'form': form, 'profile': profile})

    def post(self, request, pk):
        profile = get_object_or_404(self.model, pk=pk)
        form = self.form_class(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect(reverse('profiles_list'))  # Replace 'profiles_list' with your profiles list view name
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
            return Response({"refresh": str(refresh), "access": access},status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
        
        
def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
          
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'accounts/sign_in.html', {'title': 'Login'})

def logout_view(request):
    logout(request)
    return redirect('login')

