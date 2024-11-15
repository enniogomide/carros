from django import forms
from cars.models import Car

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self): # clean_nome do campo
        value = self.cleaned_data.get('value')
        if value and value < 20000:
            self.add_error('value', 'Valor mínimo para venda é de R$ 20.000,00')
        return value
    
    def clean_photo(self): # clean_nome do campo
        photo = self.cleaned_data.get('photo')
        if not photo:
            self.add_error('photo', 'Tem que carregar foto')
        return photo
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error('factory_year', 'O ano do carro não pode ser menor que 1975')
        return factory_year