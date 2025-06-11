from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Result

class ResultAdminForm(forms.ModelForm):
    selection_process = forms.CharField(widget=CKEditorWidget())
    eligibility_criteria = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Result
        fields = "__all__"
