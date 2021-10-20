from django import forms

from .models import Drone


class DroneForm(forms.ModelForm):
    class Meta:
        model = Drone
        fields = ['image', 'name', 'price', 'description', 'brand', 'serial_number',
                  'camera_model', 'camera_megapixel', 'camera_brand', 'camera_brand_filter'
                  ]
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'serial_number': forms.TextInput(attrs={'class': 'form-control'}),
            'camera_model': forms.TextInput(attrs={'class': 'form-control'}),
            'camera_megapixel': forms.TextInput(attrs={'class': 'form-control'}),
            'camera_brand': forms.TextInput(attrs={'class': 'form-control'}),
            'camera_brand_filter': forms.Select(attrs={'class': 'form-control'}),
        }
