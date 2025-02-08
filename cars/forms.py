from django import forms
from cars.models import Car

class CarModelForm(forms.ModelForm):
    class Meta:
        model  = Car
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 5:
            self.add_error('value', 'Valor mínimo da peça é de R$5.0 ')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 2000:
            self.add_error('factory_year', 'Sistema não permite cadastrar peças com ano inferior a 2000')
        return factory_year