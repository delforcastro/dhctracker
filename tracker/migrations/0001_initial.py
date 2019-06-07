# Generated by Django 2.2 on 2019-06-02 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(max_length=150)),
                ('relacion_iva', models.CharField(choices=[('Consumidor Final', 'Consumidor final'), ('Inscripto IVA', 'Inscripto IVA'), ('Monotributista', 'Monotributista'), ('Exento', 'Exento')], default='Consumidor Final', max_length=30)),
                ('id_impositivo', models.CharField(blank=True, max_length=20)),
                ('direccion', models.CharField(blank=True, max_length=200)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('telefono', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_ingreso', models.DateTimeField(verbose_name='fecha_ingreso')),
                ('fecha_cierre', models.DateTimeField(verbose_name='fecha_cierre')),
                ('tipo', models.CharField(choices=[('Software', 'Software'), ('Hardware', 'Hardware'), ('Config', 'Configuración'), ('Asesor', 'Asesoría'), ('Otra', 'Otra')], default='Software', max_length=15)),
                ('detalle', models.CharField(max_length=100)),
                ('importe', models.DecimalField(decimal_places=2, max_digits=10)),
                ('facturado', models.BooleanField(default=False)),
                ('cobrado', models.BooleanField(default=False)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tracker.Cliente')),
            ],
        ),
    ]
