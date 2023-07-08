from django import forms
g=[('male','MALE'),('female','FEMALE')]
c=[('python','PYTHON'),('SQL','SQL'),('django','DJANGO')]
class signupform(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    email=forms.EmailField()
    pw=forms.CharField(widget=forms.PasswordInput)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    courses=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)