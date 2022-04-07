from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):

    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name='categoria'
        verbose_name_plural='categorias'

    def __str__(self):
        return self.nombre

class Post(models.Model):

    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='blog', null=True, blank=True)
    #recordar que null y blank es para que la imagen quede opcional de subir.
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    #con la instruccion autor le indicamos a django que cuando el autor 
    #se vaya, se borren todos los posts que ha creado.
    categorias=models.ManyToManyField(Categoria)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:

        verbose_name='post'
        verbose_name_plural='posts'

    def __str__(self):
        return self.titulo