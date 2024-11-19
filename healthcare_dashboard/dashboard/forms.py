from django import forms

class HealthcareForm(forms.Form):
    name = forms.CharField(
        max_length=100, 
        label="Name", 
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your name', 'class': 'form-control'
        })
    )
    age = forms.ChoiceField(
        label="Age",
        choices=[(i, i) for i in range(1, 101)],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    file = forms.FileField(
        label="Upload File", 
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control'
        })
    )
