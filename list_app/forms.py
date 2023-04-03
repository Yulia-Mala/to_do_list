from django import forms

from list_app.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    text = {"placeholder": "YYYY-MM-DD HH:MM:SS"}
    deadline = forms.DateTimeField(widget=forms.TextInput(attrs=text))

    class Meta:
        model = Task
        fields = "__all__"
