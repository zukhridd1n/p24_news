from ckeditor.widgets import CKEditorWidget
from django.core.exceptions import ValidationError
from django.forms import Form, ModelForm, CharField, PasswordInput

from apps.account.models import Account, Feed


class SubscribeForm(ModelForm):
    password = CharField(widget=PasswordInput)
    confirm_password = CharField(widget=PasswordInput)

    def clean_confirm_password(self):
        if self.cleaned_data.get("password") != self.cleaned_data.get("confirm_password"):
            raise ValidationError("Passwords must be match")

    def save(self, commit=True):
        user: Account = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.is_subscribe = True
        user.save()
        return user

    class Meta:
        model = Account
        fields = ("first_name", "last_name", "username", "email", "password", "confirm_password",)

class FeedForm(ModelForm):
    def save(self, user, commit=True):
        feed = super().save(commit=False)
        feed.account = user
        feed.save()
        return feed

    class Meta:
        model = Feed
        exclude = ('account',)


class LoginForm(Form):
    username = CharField()
    password = CharField(widget=PasswordInput())
