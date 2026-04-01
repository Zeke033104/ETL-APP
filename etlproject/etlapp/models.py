from django.db import models

# RAW table — stores data as-is from CSV
class RawStudent(models.Model):
    student_id = models.CharField(max_length=20)
    name       = models.CharField(max_length=100)
    course     = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.student_id} - {self.name}"


# CLEAN table — stores transformed/validated data
class CleanStudent(models.Model):
    student_id = models.CharField(max_length=20)
    name       = models.CharField(max_length=100)
    course     = models.CharField(max_length=100)
    is_valid   = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.student_id} - {self.name}"