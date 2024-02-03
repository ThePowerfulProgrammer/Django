from django import forms

# Class to create a comment form
class CommentForm(forms.Form):
    author = forms.CharField(required=True,
                              max_length=40,
                              widget=forms.TextInput(
                                  attrs={"class":"form-control", 
                                         "placeholder":"Your Name",}
                                ),
                              )
    body = forms.CharField(required=True,
        widget=forms.Textarea(
            attrs={"class":"form-control",
                   "placeholder":"Leave a comment",}
        )
    )
    
    