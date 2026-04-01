import csv
from .models import RawStudent, CleanStudent

def run_etl():
    # --- EXTRACT ---
    RawStudent.objects.all().delete()   # clear old raw data
    CleanStudent.objects.all().delete() # clear old clean data

    with open("students.csv", "r") as f:
        reader = csv.DictReader(f)
        raw_records = []
        for row in reader:
            raw_records.append(RawStudent(
                student_id = row['id'],
                name       = row['name'],
                course     = row['course'],
            ))
        RawStudent.objects.bulk_create(raw_records)

    # --- TRANSFORM ---
    clean_records = []
    for raw in RawStudent.objects.all():
        name   = raw.name.strip()   if raw.name   else "Unknown"
        course = raw.course.strip() if raw.course else "Undeclared"
        is_valid = name != "Unknown" and course != "Undeclared"

        clean_records.append(CleanStudent(
            student_id = raw.student_id,
            name       = name,
            course     = course,
            is_valid   = is_valid,
        ))

    # --- LOAD ---
    CleanStudent.objects.bulk_create(clean_records)