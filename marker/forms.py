from django.forms import ModelForm
from .models import imageUpload


class photoUpload(ModelForm):
    class Meta:
        model = imageUpload
        fields = '__all__'