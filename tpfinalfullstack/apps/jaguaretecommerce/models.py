from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length= 30)
    descripcion = models.TextField()


class Producto(models.Model):
    titulo = models.CharField(max_length = 40)
    imagen = models.TextField()
    descripcion = models.TextField()
    precio = models.TextField()
    categoria_pertenece = models.ForeignKey(Categoria, on_delete=models.PROTECT)


class Usuario(models.Model):
    email = models.EmailField()
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    nombreUsuario = models.CharField(max_length=20)
    password = models.TextField()
    direccion = models.TextField()


class Carrito(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.PROTECT) 
    lista_productos = models.ManyToManyField(Producto)
    total_carrito = models.CharField(max_length=10)


class Admin(models.Model):
    userAdmin = models.OneToOneField(Usuario, on_delete = models.CASCADE)
    fechaAlta = models.DateField()
