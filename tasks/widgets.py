from django.forms.widgets import ClearableFileInput
from django.utils.safestring import mark_safe

class MultipleFileInput(ClearableFileInput):
    def render(self, name, value, attrs=None, renderer=None):
        substitutions = {
            'input_type': 'file',
            'name': name,
        }
        template = '%(input)s'
        return mark_safe(template % substitutions)
