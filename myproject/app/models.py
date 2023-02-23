from django.db import models

# Create your models here.


from django.contrib.auth.models import User

class common_table(models.Model):
    created_by = models.ForeignKey(User, related_name="%(app_label)s_%(class)s_ownership",on_delete=models.CASCADE,null=True)
    created_dt = models.DateField(auto_now=True)
    updated_by =  models.ForeignKey(User, related_name="%(app_label)s_%(class)s_ownership1",on_delete=models.CASCADE,null=True)
    updated_dt = models.DateField(null=True)
    created_tm = models.TimeField(auto_now=True)
    updated_tm = models.TimeField(null=True)
    status = models.CharField(max_length=10, null=True)

    class Meta:
        abstract = True


class Class_master(common_table):
    name  = models.CharField(max_length=25,null=True)

class Subject_master(common_table):
    name = models.CharField(max_length=25,null=True)


class Class_Mapping_subject(common_table):
    class_id = models.ForeignKey(Class_master,related_name='Class_Mapping_subject_class_id',on_delete=models.CASCADE,null=True)
    SUBJECT_id = models.ForeignKey(Subject_master,related_name='Class_Mapping_subject_subject_id',on_delete=models.CASCADE,null=True)

class Student_details(common_table):
    user_auth = models.OneToOneField(User,related_name='Student_details_auth_id',on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=25,null=True)
    address = models.TextField(null=True)
    email = models.CharField(max_length=25,null=True)
    gender = models.CharField(max_length=25,null=True)
    date_of_birth = models.DateField(null=True)
    pic = models.FileField(upload_to='student_pic',null=True)
    class_id = models.ForeignKey(Class_master,related_name='Student_details_class_id',on_delete=models.CASCADE,null=True) 
    roll_no = models.CharField(max_length=25,null=True)



class Question_bank(common_table):
    question = models.TextField()
    subject_id = models.ForeignKey(Subject_master,related_name='Question_bank_subject_id',on_delete=models.CASCADE,null=True) 
    option_A = models.CharField(max_length=25,null=True)
    option_B = models.CharField(max_length=25,null=True)
    option_C = models.CharField(max_length=25,null=True)
    option_D = models.CharField(max_length=25,null=True)
    answer = models.CharField(max_length=25,null=True)
    mark = models.IntegerField(null=False)



class Exam_master(common_table):
    exam_name = models.CharField(max_length=25,null=True)
    class_id = models.ForeignKey(Class_master,related_name='Exam_master_class_id',on_delete=models.CASCADE,null=True) 
    duration = models.CharField(max_length=25,null=True)


class Multiple_exam_details(common_table):
    exam_id = models.ForeignKey(Exam_master,related_name='Multiple_exam_details_exam_id',on_delete=models.CASCADE,null=True) 
    subject_id = models.ForeignKey(Subject_master,related_name='Multiple_exam_details_subject_id',on_delete=models.CASCADE,null=True) 
    exam_dt = models.DateField()
    exam_tm = models.TimeField()
    total_que = models.IntegerField()
    question_type = models.CharField(max_length=25,null=True)
