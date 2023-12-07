from django import forms

class TodoForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)
    due_date = forms.DateField(required=False)
    tags = forms.CharField(required=False)
    status = forms.ChoiceField(choices=[('OPEN', 'Open'), ('WORKING', 'Working'), ('DONE', 'Done'), ('OVERDUE', 'Overdue')], required=True)
