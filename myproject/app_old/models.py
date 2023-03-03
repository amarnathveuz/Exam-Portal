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


class Exam_general_instruction(common_table):
    exam_id = models.ForeignKey(Exam_master,related_name='Exam_general_instruction_exam_id',on_delete=models.CASCADE,null=True) 
    instruction = models.TextField()
    


class Multiple_exam_details(common_table):
    exam_id = models.ForeignKey(Exam_master,related_name='Multiple_exam_details_exam_id',on_delete=models.CASCADE,null=True) 
    subject_id = models.ForeignKey(Subject_master,related_name='Multiple_exam_details_subject_id',on_delete=models.CASCADE,null=True) 
    exam_dt = models.DateField()
    exam_tm = models.TimeField()
    total_que = models.IntegerField()
    question_type = models.CharField(max_length=25,null=True)


class User_details(common_table):
    user_auth = models.OneToOneField(User,related_name='User_details_auth_id',on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=25,null=True)
    contact_no = models.CharField(max_length=25,null=True)
    email = models.CharField(max_length=25,null=True)
    pic = models.FileField(upload_to='user_pic')
    





# ------------------new exam creation model------------------------

layout_choice = (
    ("0","One page with all the questions"),
    ("1","One page per section"),
    ("2","One page per question")
)

progression_choices =(
    ("Percentage","Percentage"),
    ("Number","Number")
)

selection_choices =(
    ("All questions","All questions"),
    ("Randomized per section","Randomized per section")
)

scoring_choices =(
    ("0","No scoring"),
    ("1","Scoring with answers at the end"),
    ("2","Scoring without answers at the end")
)

access_choices =(
    ("0","Anyone with the link"),
    ("1","Invited people only"),
   
)

section_choices =(
    ("Section","Section"),
    ("Question","Question"),
   
)



class Main_Exam_Master(common_table):
    Exam_title = models.CharField(max_length=50,null=True)
    responsible_person = models.ForeignKey(User,related_name='Main_Exam_Master_auth_id',on_delete=models.CASCADE,null=True)
    background_image = models.FileField(upload_to='exam_background',null=True)
    start_message = models.TextField()
    end_message = models.TextField()
    layout = models.CharField(max_length=25,choices=layout_choice,null=True)
    progression_mode = models.CharField(max_length=25,choices=progression_choices,null=True)
    Exam_time_limit = models.TimeField(null=True)
    selection_mode = models.CharField(max_length=25,choices=selection_choices,null=True)
    scoring_mode = models.CharField(max_length=25,choices=scoring_choices,null=True)
    access_mode = models.CharField(max_length=25,choices=access_choices,null=True)
    Login_required = models.BooleanField(null=True)
    attempt_limit = models.IntegerField(null=True)

question_type_choices =(
    ("Radio","Multiple choice: only one answer"),
    ("Checkbox","Multiple choice: multiple answers allowed"),
   
)


class Main_Question_Bank(common_table):
    Question = models.CharField(max_length=50,null=True)
    Imagefield = models.FileField(upload_to='Question_Bank_image',null=True)
    Question_type = models.CharField(max_length=20,choices=question_type_choices,null=True)
    Description =  models.TextField(null=True)
    manadatory = models.BooleanField(default=False)
    comments = models.CharField(max_length=25,null=True)
    total_mark = models.IntegerField(null=True)
    answer_id =  models.ManyToManyField('Question_Bank_multiple_choice', blank=True,related_name="Answer_master_id")



class Main_Exam_section(common_table):
    Exam_id = models.ForeignKey(Main_Exam_Master,related_name ="Main_Exam_section_exam_id",on_delete=models.CASCADE,null=True)
    section_title = models.CharField(max_length=50,null=True)
    section_type = models.CharField(max_length=20,choices=section_choices,null=True)
    Question_bank_id = models.ForeignKey(Main_Question_Bank,related_name='Main_Exam_Master_question_id',on_delete=models.CASCADE,null=True)

class Question_Bank_multiple_choice(common_table):
    Question_id = models.ForeignKey(Main_Question_Bank,related_name ="Exam_section_exam_id",on_delete=models.CASCADE,null=True)
    choice = models.CharField(max_length=50,null=True)
    Imagefield = models.FileField(upload_to='Question_Bank_multiple',null=True)
    Mark = models.IntegerField(null=True)
    result_status = models.BooleanField(default=False)

class Section_Question_Mapping(common_table):
    Section_id = models.ForeignKey(Main_Exam_section,related_name ="Section_Question_Mapping_id",on_delete=models.CASCADE,null=True)
    Question_id = models.ForeignKey(Main_Question_Bank,related_name ="Question_Bank_id",on_delete=models.CASCADE,null=True)


Exam_start_field=(
    ("selection","selection"),
    ("Text Input","Text Input"),
   
)


class Exam_inital_field(common_table):
    Exam_id = models.ForeignKey(Main_Exam_Master,related_name ="Exam_inital_field_exam_id",on_delete=models.CASCADE,null=True)
    title = models.TextField()
    field_type = models.CharField(max_length=20,choices=Exam_start_field,null=True)

class Exam_inital_field_choice(common_table):
    initial_field_id = models.ForeignKey(Exam_inital_field,related_name ="Exam_inital_field_id",on_delete=models.CASCADE,null=True)
    choice_name = models.CharField(max_length=25,null=True)


from django.utils.translation import gettext as _

class Book(models.Model):
    title = models.CharField(_('Title'), max_length=100)
    author = models.CharField(_('Author'), max_length=100)