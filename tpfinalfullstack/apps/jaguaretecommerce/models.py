from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length= 30)
    descripcion = models.TextField()

    def __str__(self):
        return f'{self.id} - {self.nombre}'
    

class Producto(models.Model):
    titulo = models.CharField(max_length = 40)
    imagen = models.ImageField(upload_to='products/', default='product_blank.png')
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoriaPertenece = models.ForeignKey(Categoria, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.id} - {self.titulo}'
    


class Usuario(models.Model):
    email = models.EmailField(primary_key=True)
    nombres = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    nombreUsuario = models.CharField(max_length=20)
    password = models.TextField()
    direccion = models.TextField()

    def __str__(self):
        return f'{self.email} - {self.nombreUsuario}'
    


class Carrito(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.PROTECT) 
    listaProductos = models.ForeignKey(Producto, null=True, on_delete=models.PROTECT)
    totalCarrito = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.id} - {self.cliente} - {self.totalCarrito}'
    


class Admin(models.Model):
    userAdmin = models.OneToOneField(Usuario, on_delete = models.CASCADE)
    fechaAlta = models.DateField()

    def __str__(self):
        return f'{self.id} - {self.userAdmin}'
    
