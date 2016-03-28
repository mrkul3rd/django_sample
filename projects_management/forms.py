from django import forms
from .models import Project, Employee

class ProjectForm(forms.ModelForm):
    project_name = forms.CharField(max_length=50, help_text="Project name", widget=forms.TextInput(attrs={'class': "form-control"}))

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Project
        fields = ('project_name',)

class EmployeeForm(forms.ModelForm):
    emp_name = forms.CharField(max_length=50, help_text="Employee name", widget=forms.TextInput(attrs={'class': "form-control"}))
    project = forms.ModelChoiceField(queryset=Project.objects.all(), help_text="Project", widget=forms.Select(attrs={'class': "form-control"}))

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Employee
        fields = ('emp_name', 'project',)

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the project field from the form,
        #exclude = ('Project',)
        #or specify the fields to include (i.e. not include the category field)
        #fields = ('title', 'url', 'views')
    
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        # If url is not empty and doesn't start with 'http://', prepend 'http://'
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

        return cleaned_data