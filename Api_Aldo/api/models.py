from django.db import models

# Create your models here.

class Genero(models.Model):
    idGenero = models.IntegerField(primary_key=True,db_column='idGenero')
    tipoGenero = models.CharField(max_length=100,db_column='tipoGenero')
    class Meta:
        db_table='Genero'

class Alumno(models.Model):
    idAlumnos = models.IntegerField(primary_key=True,db_column='idAlumno')
    nameAlumno = models.CharField(max_length=100,db_column='nameAlumno')
    fk_genero = models.ForeignKey(Genero,default=1,on_delete=models.CASCADE,db_column='fk_genero')
    class Meta:
        db_table='Alumnos'

class Alumno_has_Genero(models.Model):
    fk_Alumno = models.ForeignKey(Alumno,default=1,on_delete=models.CASCADE,db_column='fk_alumno')
    fk_Genero = models.ForeignKey(Genero,default=1,on_delete=models.CASCADE,db_column='fk_genero')
    class Meta:
        db_table='alumno_has_genero'