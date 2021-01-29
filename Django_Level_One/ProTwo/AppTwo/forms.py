from django import forms
from django.core import validators
from AppTwo.models import Users

class FormName(forms.ModelForm):
    botcatcher = forms.CharField(required = False, widget=forms.HiddenInput,
    validators=[validators.MaxLengthValidator(0)]);

    class Meta:
        model = Users
        fields = "__all__"

    def clean(self):
        all_clean_data = super().clean()
        print('First name: '+all_clean_data['first_name'])
        print('Last name: '+all_clean_data['last_name'])

    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher) > 0:
            raise forms.ValidationError('the bot is catched!')
        return botcatcher
