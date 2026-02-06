from django.db import models

class User(models.Model):
    name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=10)

class Administration(models.Model):
    class AdminTypes(models.IntegerChoices):
        SUPERADMIN = (1, "Super Admin")
        TRAINER = (2, "Entrenador")

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.IntegerField(
        choices=AdminTypes.choices,
        default=AdminTypes.TRAINER,
        verbose_name="Admin type"
    )

class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=600, null=True, blank=True)
    birthdate = models.DateField(
        verbose_name="Fecha De Cumpleaños",
        null=True, blank=True
    )

class Exercise(models.Model):
    name = models.CharField(max_length=225)
    description = models.CharField(max_length=600)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Category(models.Model):
    class ExerciseTypes(models.IntegerChoices):
        PECHO = (1, "Pecho")
        ESPALDA = (2, "Espalda")
        PIERNA = (3, "Pierna")
        HOMBRO = (4, "Hombro")
        BRAZO = (5, "Brazo")

    name = models.CharField(max_length=225)
    type = models.IntegerField(
        choices=ExerciseTypes.choices,
        verbose_name="Type Of Muscle"
    )

    def __str__(self):
        return self.name
