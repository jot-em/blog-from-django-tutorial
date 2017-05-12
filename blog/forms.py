from django import forms
from .models import Post
import re
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class PostForm(forms.ModelForm):
	title = forms.CharField(max_length=10, label="Tytuł", required=False)
	text = forms.CharField(max_length=10, label="Tekst", required=False)
	CATEGORIES_CHOICES = (('music', 'Kosmos'),('science', 'Technologia'), ('sport', 'Sprzęt'), ('others', 'Inne'))
	categories = forms.ChoiceField(label='Kategoria', choices=CATEGORIES_CHOICES)
	author_invisible = forms.BooleanField(label='Nie wyświetlaj, kto jest autorem', required=False)
	
	class Meta:
		model=Post
		fields=('title', 'categories', 'text', 'author_invisible')

 
class RegistrationForm(forms.Form):
 
    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=3)), label=_("Nazwa użytkownika"), 
    	error_messages={ 'invalid': _("Nazwa zawierać może wyłącznie litery, cyfry i znak podkreślenia.") })
    email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Adres e-mail"), error_messages={ 'invalid': _("Niepoprawny adres e-mail.") })
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Hasło"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Powtórz hasło"))

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("Użytkownik o podanej nazwie już istnieje. Podaj inną nazwę."))
 
    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("Hasła nie są identyczne."))
        return self.cleaned_data

