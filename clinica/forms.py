# clinica/forms.py
from django import forms
from .models import Consulta, Medico

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['paciente', 'data', 'medico', 'status']
        widgets = {
            'data': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        super(ConsultaForm, self).__init__(*args, **kwargs)
        self.fields['medico'].queryset = Medico.objects.all()  # Preencher médicos disponíveis


