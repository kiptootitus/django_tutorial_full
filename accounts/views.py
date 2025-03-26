from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from accounts.models import Profile

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
