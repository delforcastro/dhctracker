from django.db import models
from django.utils import timezone


# Create your models here.

#Creo modelo de cliente

#Referencia de choices en CharField:
#https://docs.djangoproject.com/en/2.2/ref/models/fields/


class Cliente (models.Model):
    RELACIONES_IVA = [
        ('Consumidor Final', 'Consumidor final'),
        ('Inscripto IVA', 'Inscripto IVA'),
        ('Monotributista', 'Monotributista'),
        ('Exento', 'Exento'),
    ]

    denominacion = models.CharField(max_length=150)
    relacion_iva = models.CharField(max_length=30,
                                    choices=RELACIONES_IVA,
                                    default='Consumidor Final'
                                    )
    id_impositivo = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    telefono = models.CharField (max_length=30, blank=True)


    def __str__(self):
        return self.denominacion

class Tarea (models.Model):
    TIPO_TAREA = [
        ('Software', 'Software'),
        ('Hardware', 'Hardware'),
        ('Config', 'Configuración'),
        ('Asesor', 'Asesoría'),
        ('Otra', 'Otra')

    ]
    cliente = models.ForeignKey(Cliente, null=True, on_delete=models.CASCADE)
    fecha_ingreso = models.DateTimeField('fecha_ingreso')
    fecha_cierre = models.DateTimeField('fecha_cierre')
    tipo = models.CharField(max_length=15,
                            choices=TIPO_TAREA,
                            default='Software'
                            )
    detalle = models.CharField(max_length=100)
    importe = models.DecimalField (max_digits=10, decimal_places=2)
    facturado = models.BooleanField(default=False)
    cobrado = models.BooleanField(default=False)


    def __str__(self):
        return self.detalle






