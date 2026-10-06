from django import forms
from .models import RoommateProfile

class RoommateProfileForm(forms.ModelForm):
    class Meta:
        model = RoommateProfile
        fields = ['name','age','city','budget','sleep','cleanliness','food','smoking','social','noise','guests','cooking','study_work','bio']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Short intro, habits, preferences...'}),
            'budget': forms.NumberInput(attrs={'min': 1000, 'step': 500}),
            'age': forms.NumberInput(attrs={'min': 16, 'max': 80}),
        }
