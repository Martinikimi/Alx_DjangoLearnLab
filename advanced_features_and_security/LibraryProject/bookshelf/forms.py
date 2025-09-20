from django import forms

class ExampleForm(forms.Form):
    """
    ExampleForm is a simple Django form for demonstration purposes.
    Add any fields you need here for testing or assignment purposes.
    """
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
