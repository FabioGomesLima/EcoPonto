from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuarios(AbstractUser):
    email = models.EmailField('Email', max_length=100, unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  

    def __str__(self):
        return self.username

class PontosDeColeta(models.Model):
    descricao = models.TextField('Descrição', max_length=400)
    imagem = models.ImageField('Imagem', upload_to='uploads/', null=True, blank=True)
    tipo = models.CharField('Tipo', max_length=100)
    usuario = models.ForeignKey(Usuarios, on_delete=models.PROTECT) 

    def __str__(self):
        return f"{self.tipo} - {self.descricao[:30]}" 
    
    
class PontoColeta(models.Model):
     nome = models.CharField(max_length=100)
     endereco = models.TextField()
     latitude = models.FloatField()
     longitude = models.FloatField()
    
     TIPOS_RESIDUO = [
        ("eletronicos", "Eletrônicos"),
        ("plastico", "Plástico"),
        ("vidro", "Vidro"),
        ("metal", "Metal"),
        ("organico", "Orgânico"),
    ]

     tipo_residuo = models.CharField(
        max_length=100,
        choices=TIPOS_RESIDUO
    )

     def __str__(self):
        return self.nome

