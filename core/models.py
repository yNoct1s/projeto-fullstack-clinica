from django.db import models

class Medico(models.Model):
    nome = models.CharField(max_length=100)
    crm = models.CharField(max_length=20)
    especialidade = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nome} ({self.especialidade})"

class Consulta(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    paciente_nome = models.CharField(max_length=100)
    data_consulta = models.DateTimeField()
    motivo = models.TextField()
    
    def __str__(self):
        return f"{self.paciente_nome} - {self.data_consulta}"