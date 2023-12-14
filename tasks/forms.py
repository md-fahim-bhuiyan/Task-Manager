from django import forms
from multiupload.fields import MultiFileField
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'is_complete']

    # # Replace ImageField with MultiFileField for multiple file uploads
    photos = MultiFileField(min_num=1, max_num=5,max_file_size=1024 * 1024 * 5,  required=False)
