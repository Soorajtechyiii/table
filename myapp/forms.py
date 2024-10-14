from django import forms
class Name(forms.Form):
    user_name=forms.CharField (label='enter Username:',max_length=50)
    Mail_id=forms.EmailField(label='enter email id',max_length=30)
  