from django.db import models
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Create your models here.

class imageUpload(models.Model):
    title = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = 'media')
    date_uploaded = models.DateTimeField(auto_now = True)


    def __str__(self):
        return self.title


    def save(self):
        super().save()  
        image = Image.open(self.image.path)
        width, height = image.size
        draw = ImageDraw.Draw(image) 
        text = "@denno"
        font = ImageFont.truetype('arial.ttf', 500)
        textwidth, textheight = draw.textsize(text, font)
        x = width - textwidth*2  
        y = height - textheight*2 
        draw.text((x, y), text, font=font) 
        out = image.filter(ImageFilter.DETAIL)
        out.save(self.image.path)
        