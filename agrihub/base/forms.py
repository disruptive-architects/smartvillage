from django import forms

class MyForm(forms.Form):
    from_address = forms.CharField(max_length=100)
    to_address = forms.CharField(max_length=50)
    object_details = forms.CharField(widget=forms.Textarea)
    phone_number = forms.CharField(max_length=100)
    
    def __init__(self, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'