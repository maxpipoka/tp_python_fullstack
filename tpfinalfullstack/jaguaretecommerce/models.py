from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = CharField(max_length= 40)
    descripcion = TextField()


class Producto(models.Model):
    titulo = CharField(max_length = 50)
    imagen = TextField()
    descripcion =
    precio =
    categoria_pertenece =


class Carrito(models.Model):
    usuario = 
    lista_productos = 
    total_carrito = 
