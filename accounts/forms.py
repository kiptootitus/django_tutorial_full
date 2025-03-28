from django import forms
from accounts.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'address', 'email', 'phone']  # Replace with actual fields of the Profile model