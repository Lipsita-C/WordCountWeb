
from django import forms
from home.models import Resume

class ResumeForm(forms.ModelForm):

   class Meta:
      model = Resume
      fields = ('email','name','file')

    