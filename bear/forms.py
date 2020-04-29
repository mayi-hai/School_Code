from django import forms


class UserForm(forms.Form):
    account = forms.CharField(label="account", max_length=128)
    password = forms.CharField(label="password", max_length=256, widget=forms.PasswordInput)
    usertype = forms.IntegerField(label="usertype")


class ResetForm(forms.Form):
    account = forms.CharField(label="account", max_length=128)
    password = forms.CharField(label="password", max_length=256, widget=forms.PasswordInput)
    question_id = forms.CharField(label="question_id", max_length=128)
    answer = forms.CharField(label="answer", max_length=128)
    usertype = forms.IntegerField(label="usertype")
