from django import forms


class SearchForm(forms.Form):
    keyword = forms.CharField(max_length = 25)
"""
class EmailAddressForm(form.Form):
    address = forms.CharField(max_length = 50,blank = False )

    def addressValidation():
        try :
            validate_mail(address);
            return True
        except:
            return False

class EmailSubjectForm(forms.Form):
    subject = forms.CharField(max_length = 50, blank = False)

class EmailTextForm(forms.Form):
    text = forms.CharField(max_length = 500, blank = False)
"""
class ContactForm(forms.Form):
    address = forms.EmailField(required=True)
    subject = forms.CharField(required = True)
    body = forms.CharField(widget=forms.Textarea)
