from django import forms

class StudentForm(forms.Form):
    c=[('Python','Python'),('Java',"Java")]
    g=[('male','MALE'),('female',"FEMALE")]
    p=[('html','HTML'),('css',"CSS"),('javascript','JAVASCRIPT')]
    l=[('telugu','TELUGU'),('kannada',"KANNADA"),('tamil','TAMIL')]
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    email=forms.EmailField()
    url=forms.URLField()
    possward=forms.CharField(max_length=100,widget=forms.PasswordInput)
    textarea=forms.CharField(max_length=300,widget=forms.Textarea(attrs={'cols':5,'rows':2}))
    date_time=forms.DateTimeField()
    gender=forms.ChoiceField(choices=g)
    course=forms.ChoiceField(choices=c,widget=forms.RadioSelect)
    web=forms.MultipleChoiceField(choices=p)
    languages=forms.MultipleChoiceField(choices=l,widget=forms.CheckboxSelectMultiple)

