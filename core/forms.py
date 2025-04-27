from django import forms
from .models import Client, Enrollment, Program

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'date_of_birth', 'gender', 'contact_info', 'address']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'contact_info': forms.TextInput(attrs={'placeholder': 'Phone or Email'}),
            'address': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

class EnrollmentForm(forms.ModelForm):
    program = forms.ModelChoiceField(queryset=Program.objects.all(), empty_label="Select a Program")

    class Meta:
        model = Enrollment
        fields = ['program']

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['name', 'description'] 

        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Program description...'}),
        }

    