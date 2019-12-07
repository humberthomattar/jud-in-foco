from django.db import models

# Create your models here.
class Teenager(models.Model):
    
    name = models.CharField(
        verbose_name = 'Nome',
        max_length = 255,
        null = False ,
        blank = False
    )

    name_mother = models.CharField(
        verbose_name = 'Nome da mãe',
        max_length = 255,
        null = False,
        blank = False
    )

    name_father = models.CharField(
        verbose_name = 'Nome do pai',
        max_length = 255,
        null = True,
        blank = True
    )

    date_birth = models.DateField(
        verbose_name = 'Data de Nascimento',
        null = False,
        blank = False,
        auto_now= False
    )

    type_sex = models.CharField(
        verbose_name = 'Sexo',
        max_length = 20,
        null = True,
        blank = True
    )

    notes = models.CharField(
        verbose_name = 'Observações',
        max_length = 20,
        null = True,
        blank = True
    )

    address = models.CharField(
        verbose_name = 'Endereço',
        max_length = 355,
        null = True,
        blank = True
    )
    
    is_active = models.BooleanField(
        verbose_name = 'Ativo?',
        default= True
    )

    objects = models.Manager()