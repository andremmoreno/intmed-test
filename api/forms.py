from django import forms
from api.models import Schedule, ScheduleHours
import datetime

class ScheduleForm(forms.ModelForm):
    horarios = forms.ModelMultipleChoiceField(
      queryset = ScheduleHours.objects,
      widget = forms.CheckboxSelectMultiple(),
      required = False,
    )
    
    def clean(self):
        day = self.cleaned_data['dia']
        medic = self.cleaned_data['medico']

        agenda = Schedule.objects.filter(medico=medic, dia=day)

        if day < datetime.date.today():
            raise forms.ValidationError("Data inválida")
        
        if agenda:
            raise forms.ValidationError("Agenda já criada")
