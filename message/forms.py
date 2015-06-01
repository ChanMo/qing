from django.form import ModelForm
from .models import Message

class MessageForm(ModelForm):
    class Meta:
        model = Message
        #fields = ['site', 'name', 'mobile']
        fields = '__all__'
