from django.forms import ModelForm, ValidationError
from .models import *
from django.contrib import admin
from PIL import Image
from django.utils.safestring import mark_safe


class NotebookAdminForm(ModelForm):

    MIN_RESOLUTION = (300, 300)
    MAX_RESOLUTION = (800, 800)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe('<span style = "color: red; font-size: 14px;"> Загружайте изображения мин разрешением {}x{} </span>'.format(*self.MIN_RESOLUTION))

    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_height, min_width = Product.MIN_RESOLUTION
        max_height, max_width = self.MAX_RESOLUTION
        if img.height < min_height or img.width < min_width:
            raise ValidationError('Слишком маленькое изображение ')
        if img.height > max_height or img.width > max_width:
            raise ValidationError('Слишком большое изображение ')
        if image.size > Product.MAX_IMAGE_SIZE:
            raise ValidationError('Слишком большого размера изображение, максимум 3мб ')

        return image



class adminT(admin.ModelAdmin):
    form = NotebookAdminForm



admin.site.register(Category)
admin.site.register(Notebook)
admin.site.register(Smartphone, adminT)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)


