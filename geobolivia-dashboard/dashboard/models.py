from django.db import models

class IndicadorClimatico(models.Model):
    CATEGORIAS = [
        ('agropecuario', 'Agropecuario'),
        ('agua', 'Agua'),
        ('bosques', 'Bosques'),
    ]
    
    municipio = models.CharField(max_length=100)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    indicador = models.CharField(max_length=100)
    valor = models.FloatField()
    anio = models.IntegerField()
    
    def __str__(self):
        return f"{self.municipio} - {self.indicador}: {self.valor}"
