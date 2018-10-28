from datetime import datetime
from django.contrib.auth.models import User, Group
from django.db import models

# Create your models here.
GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)

SEMESTER_CHOICES = (
    ('I', 'Odd'),
    ('II', 'Even'),
    ('W', 'Winter Course'),
    ('S', 'Summer Course')
)

EXAM_CHOICES = (
    ('MIDSEM', 'MIDSEM'),
    ('ENDSEM', 'ENDSEM'),
    ('QUIZ', 'QUIZ')
)


def year_choices():
    return [(str(r) + "-" + str(r + 1), str(r) + "-" + str(r + 1)) for r in range(1984, datetime.utcnow().year)]


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=50, blank=False, null=False)
    sex = models.CharField(max_length=1, choices=GENDER_CHOICES)
    batch = models.IntegerField(default=datetime.utcnow().year)
    joining_date = models.DateField(null=True)
    roll_number = models.IntegerField(unique=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False, unique=True)

    class Meta:
        db_table = "student"


class Professor(models.Model):
    id = models.AutoField(primary_key=True)
    professor_name = models.CharField(max_length=50, blank=False, null=False)
    sex = models.CharField(max_length=1, choices=GENDER_CHOICES)
    joining_date = models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=False, unique=True)

    class Meta:
        db_table = "professor"


class Course(models.Model):
    subject_name = models.CharField(max_length=200)
    subject_code = models.CharField(max_length=10, unique=True)
    is_active = models.BooleanField(default=True)
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT, null=True)

    class Meta:
        db_table = "course"


class CourseGrading(models.Model):
    exam_type = models.CharField(max_length=20, choices=EXAM_CHOICES)
    weightage = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.PROTECT, null=True)

    class Meta:
        db_table = "course_grading"
        unique_together = ('exam_type', 'course')


class AcademicSession(models.Model):
    semester = models.CharField(max_length=10, choices=SEMESTER_CHOICES)
    session_year = models.CharField(max_length=10, choices=year_choices())
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "academic_session"
        unique_together = ('semester', 'session_year')


class AcademicSessionCourses(models.Model):
    academic_session = models.ForeignKey(AcademicSession, on_delete=models.PROTECT, null=False)
    course = models.ForeignKey(Course, on_delete=models.PROTECT, null=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "academic_session_course"


class EnrolledStudents(models.Model):
    academic_session_course = models.ForeignKey(AcademicSessionCourses, on_delete=models.PROTECT, null=False)
    student = models.ForeignKey(Student, on_delete=models.PROTECT, null=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "enrolled_student"


class MarkSheet(models.Model):
    enrolled_student = models.ForeignKey(EnrolledStudents, on_delete=models.PROTECT, null=False)
    course_grading = models.ForeignKey(CourseGrading, on_delete=models.PROTECT, null=False)
    marks = models.IntegerField()

    class Meta:
        db_table = "marksheet"
