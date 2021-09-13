from django.db import models

class Dotaciones(models.Model):
    codigo = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=40)
    tipo = models.CharField(max_length=50)
    sistema_operativo = models.CharField(max_length=40)
    fecha_asignado = models.DateField(blank=True, null=True)
    empleado_asignado = models.CharField(max_length=60, blank=True)
    empleado_email = models.EmailField(max_length=254, blank=True)
    def __str__ (self):
        out = f"codigo: {self.codigo}\nnombre: {self.nombre}\ntipo: {self.tipo}\n"\
            f"sistema operativo: {self.sistema_operativo}\nfecha asignado: {self.fecha_asignado}\n"\
            f"empleado asignado: {self.empleado_asignado}\nempleado email: {self.empleado_email}"
        return out
            