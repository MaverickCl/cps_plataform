from django.db import models

class FinishGood(models.Model):
    Referencia = models.CharField(max_length=40, primary_key=True)
    Descripcion = models.CharField(max_length=100)
    Estado = models.CharField(max_length=100)
    Necesidad = models.IntegerField(blank=True)
    Url = models.CharField(max_length=2083)

    def __str__(self):
        return self.Referencia

class Componente(models.Model):
    Referencia = models.CharField(max_length=40, primary_key=True)
    Descripcion = models.CharField(max_length=100)
    Estado = models.CharField(max_length=100)
    Stock = models.FloatField(blank=True)
    Necesidad = models.IntegerField(blank=True)
    Url = models.CharField(max_length=2083)
    
    def __str__(self):
        return self.Referencia

class BOM(models.Model):
    finish_good = models.ForeignKey(FinishGood, on_delete=models.CASCADE,primary_key=True)
    componente = models.ForeignKey(Componente, on_delete=models.CASCADE)
    nivel = models.IntegerField()

    class Meta:
        unique_together = (('finish_good', 'componente'),)

    def __str__(self):
        return f'{self.finish_good.Referencia} -> {self.componente.Referencia}'



    
    
    