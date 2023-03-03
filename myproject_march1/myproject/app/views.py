from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import *
# Create your views here.


def index(request):
    return render(request,'index.html')


def dashboard(request):
    return render(request,'dashboard.html')


def login_action(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        password = request.POST.get("password")
        user = authenticate(username=uname, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, str("Incorrect username or password"))
            return redirect(request.META['HTTP_REFERER'])
        


def classes(request):
    data = Class_master.objects.all()
    context = {
        'data':data
    }
    return render(request,'classes.html',context)

def create_class(request):
    if request.method == "POST":
        name = request.POST.get("name")
        try:
            data = Class_master.objects.get(name=name)
            messages.error(request, str("alredy exists"))
        except:

            data_save = Class_master.objects.create(name=name,created_by=request.user)
            messages.success(request, str("success"))
        return redirect(request.META['HTTP_REFERER'])
    return render(request,'create_class.html')

def subject(request):
    data = Subject_master.objects.all()
    context = {
        'data':data
    }
    return render(request,'subject.html',context)

def create_subject(request):
    if request.method == "POST":
        name = request.POST.get("name")
        try:
            data = Subject_master.objects.get(name=name)
            messages.error(request, str("alredy exists"))
        except:
            data_save = Subject_master.objects.create(name=name,created_by=request.user)
            messages.success(request, str("success"))
        return redirect(request.META['HTTP_REFERER'])
    return render(request,'create_subject.html')


def assign_subject(request):
    data = Class_Mapping_subject.objects.all()
    context = {
        'data':data
    }
    return render(request,'assign_subject.html',context)


def create_assign_subject(request):
    if request.method == "POST":
        class1 = request.POST.get("class1")
        subject = request.POST.get("subject")
        try:
            data = Class_Mapping_subject.objects.get(class_id_id=class1,SUBJECT_id_id=subject)
            messages.error(request, str("alredy exists"))
        except:
            data_save = Class_Mapping_subject.objects.create(class_id_id=class1,SUBJECT_id_id=subject)
            messages.success(request, str("success"))
        return redirect(request.META['HTTP_REFERER'])
    class_data = Class_master.objects.all()
    subject_data = Subject_master.objects.all()
    context = {
        'class_data':class_data,
        'subject_data':subject_data

    }
    return render(request,'create_assign_subject.html',context)

def student(request):
    data = Student_details.objects.all()
    context = {
        'data':data
    }
    return render(request,'student.html',context)


def create_student(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        address = request.POST.get("address")
        email = request.POST.get("email")
        password = request.POST.get("password")
        gender = request.POST.get("gender")
        dob = request.POST.get("dob")
        pic = request.FILES['pic']
        if User.objects.filter(username=uname).exists():
            messages.warning(request,"Username already exists")
            return redirect(request.META['HTTP_REFERER'])
        else:
            user = User.objects.create_user(uname, password = password)
            user.save()
            data_save = Student_details.objects.create(user_auth=user,name=uname,address=address,email=email,gender=gender,date_of_birth=dob,pic=pic)
            messages.success(request, str("success"))
        return redirect(request.META['HTTP_REFERER'])
    
    return render(request,'create_student.html')

def assign_student(request):
    data = Student_details.objects.all()
    context = {
        'data':data
    }
    return render(request,'assign_student.html',context)

def create_assign_student(request):
    if request.method == "POST":
        class1 = request.POST.get("class1")
        student_id = request.POST.get("student_id")
        roll_no = request.POST.get("roll_no")
        update_data = Student_details.objects.filter(id=student_id).update(class_id_id=class1,roll_no=roll_no)
        messages.success(request, str("success"))
        return redirect(request.META['HTTP_REFERER'])
    student_data = Student_details.objects.all()
    class_data = Class_master.objects.all()
    context = {
        'student_data':student_data,
        'class_data':class_data
    }
    return render(request,'create_assign_student.html',context)

def exam(request):
    data = Exam_master.objects.all()
    context = {
        'data':data
    }
    return render(request,'exam.html',context)


def create_exam(request):
    if request.method == "POST":
        name = request.POST.get("name")
        class_name = request.POST.get("class_name")
        duration = request.POST.get("duration")
        instruction = request.POST.getlist("instruction")
        


         
        data_save = Exam_master.objects.create(exam_name=name,class_id_id=class_name,duration=duration)
        for  i in instruction:
            data_ins = Exam_general_instruction.objects.create(exam_id_id=data_save.id,instruction=i)
        messages.success(request, str("success"))
        return redirect(request.META['HTTP_REFERER'])
    data_class  = Class_master.objects.all()
    context = {
        'data_class':data_class
    }
    return render(request,'create_exam.html',context)


def exam_subject(request):
    data = Multiple_exam_details.objects.all()
    context = {
        'data':data
    }
    return render(request,'exam_subject.html',context)

def create_exam_subject(request):
    if request.method == "POST":
        exam_name = request.POST.get("exam_name")
        subject = request.POST.get("subject")
        exam_dt = request.POST.get("exam_dt")
        exam_tt = request.POST.get("exam_tt")
        total = request.POST.get("total")
        question_type = request.POST.get("question_type")
        data_save  = Multiple_exam_details.objects.create(exam_id_id=exam_name,subject_id_id=subject,exam_dt=exam_dt,exam_tm=exam_tt,total_que=total,question_type=question_type)
        messages.success(request, str("success"))
        return redirect(request.META['HTTP_REFERER'])
    data = Exam_master.objects.all()
    subject_data  =Subject_master.objects.all()
    context = {
        'data':data,
        'subject_data':subject_data
    }
    return render(request,'create_exam_subject.html',context)


def question(request):
    data = Question_bank.objects.all()
    context = {
        'data':data
    }
    return render(request,'question.html',context)


def create_question(request):
    if request.method == "POST":
        subject = request.POST.get("subject")
        question = request.POST.get("question")
        optiona = request.POST.get("optiona")
        optionb = request.POST.get("optionb")
        optionc = request.POST.get("optionc")
        optiond = request.POST.get("optiond")
        answer = request.POST.get("answer")
        result = request.POST.get("option"+answer)
        mark = request.POST.get("mark")
        demooo = request.POST.get("demooo")
        print("demooo::::::::::::",str(demooo))
        return
        data_save = Question_bank.objects.create(question=question,subject_id_id=subject,option_A=optiona,option_B=optionb,option_C=optionc,option_D=optiond,answer=result,mark=mark)
        messages.success(request, str("success"))
        return redirect(request.META['HTTP_REFERER'])
    subject_data = Subject_master.objects.all()
    context = {
        'subject_data':subject_data
    }
    return render(request,'create_question.html',context)


def user(request):
    data = User_details.objects.all()
    context = {
        'data':data
    }
    return render(request,'user.html',context)


def create_user(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        password = request.POST.get("password")
        pic = request.FILES['pic']
        if User.objects.filter(username=uname).exists():
            messages.warning(request,"Username already exists")
            return redirect(request.META['HTTP_REFERER'])
        else:
            user = User.objects.create_user(uname, password = password)
            user.save()
            data_save = User_details.objects.create(user_auth=user,name=uname,contact_no=phone,email=email,pic=pic)
            messages.success(request, str("success"))
        return redirect(request.META['HTTP_REFERER'])
    return render(request,'create_user.html')



def student_login(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        password = request.POST.get("password")
        user = authenticate(username=uname, password=password)
        if user is not None:
            login(request, user)
            return redirect('student_dashboard')
        else:
            messages.error(request, str("Incorrect username or password"))
            return redirect(request.META['HTTP_REFERER'])

    return render(request,'student_login.html')


def student_dashboard(request):
    data = Student_details.objects.get(user_auth=request.user)
    data_class_id  = data.class_id.id
    data_exam = Exam_master.objects.filter(class_id_id=data_class_id)
    context = {
        'data_exam':data_exam
    }

    return render(request,'student_dashboard.html',context)



def multiple_exam(request):
    id  = request.GET.get("id")
    data_general_instruction = Exam_general_instruction.objects.filter(exam_id_id=id)
    data = Multiple_exam_details.objects.filter(exam_id_id=id)
    context = {
        'data':data,
        'data_general_instruction':data_general_instruction
    }
    return render(request,'multiple_exam.html',context)

def exam_form(request):
    if request.method == "POST":
        question_id = request.POST.getlist("question_id")
        total_scroe_mark = 0
        total_mark = 0

        for i in question_id:
            answer = request.POST.get("q2-input"+i)
            data = Question_bank.objects.get(id=i)
            if data.answer == answer:
                total_scroe_mark+=data.mark
            
            total_mark+=data.mark


        context = {
            'total_mark':total_mark,
            'total_scroe_mark':total_scroe_mark
        }
        return render(request,'result.html',context)
            
    id = request.GET.get("id")
    data = Multiple_exam_details.objects.get(id=id)

    data_question = Question_bank.objects.filter(subject_id_id=data.subject_id.id)
    context = {
        'data':data,
        'data_question':data_question
    }
    return render(request,'exam_form.html',context)


def demo(request):
    return render(request,'demo.html')
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def demo_action(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        
        for i in data:
            print(i['name'])
            print(i['age'])
            print(type(i['age']))
       

# Amritha Updates

def main_exam(request):
    user_details = User.objects.all()
    context = {
        "user_details":user_details
    }
    return render(request,'main_exam.html',context)



def exam_save_action(request):
    if request.method == "POST":
        exam_title = request.POST.get("exam_title",False)

        section_line = request.POST.getlist("section_line")
        print("section_line::::::",section_line)
        section_line_count = request.POST.getlist("section_line_count")

        main_zip = zip(section_line,section_line_count)
        for section_title,section_count in main_zip:
            question = request.POST.getlist("question_name"+str(section_count))
            print("question::::::",question)
            question_model_name = request.POST.getlist("question_model_name"+str(section_count))
            question_zip = zip(question,question_model_name)
            for  question,model_count in question_zip:
                choice_data = request.POST.getlist("question_choice"+model_count)

        # section_title = request.POST.getlist("section_title",False)
        # section_count = request.POST.getlist("section_count",False)
        # print("section_count:::::::",section_count)
        # section_zip = zip(section_title,section_count)

        # for stitle,s_count in section_zip:
        #     print("s_count:::::::",s_count)
        #     print("stitle::::::::",stitle)
        #     question_name = request.POST.getlist("questionname"+str(s_count))
        #     print("question_name:::::::",question_name)


        exam_background = request.FILES['exam_background']
        responsible_name = request.POST.get("responsible_name",False)
        return
        


        layout = request.POST.get("layout",False)
        progression = request.POST.get("progression",False)
        exam_time_limit = request.POST.get("exam_time_limit",False)
        start_message = request.POST.get("start_message",False)
        end_message = request.POST.get("end_message",False)


        selection = request.POST.get("selection",False)
        Scoring = request.POST.get("Scoring",False)
        access_mode = request.POST.get("access_mode",False)

        login_required = request.POST.get("login_required",False)

        question_image = request.FILES['question_image']
        question_type = request.POST.get("question_type",False)

        choices = request.POST.getlist("choices",False)
        choice_image = request.FILES.getlist('choice_image')
        result_status = request.POST.getlist("result_status",False)
        Mark = request.POST.getlist("Mark",False)

        question_description = request.POST.get("question_description",False)
        question_mandatory = request.POST.get("question_mandatory",False)
        question_comment = request.POST.get("question_comment",False)

        choice_length = len(choices)

        Main_Exam_Master.objects.create(Exam_title =exam_title,responsible_person =responsible_name,)


        return redirect('main_exam')



def open_section_based_question(request):
    modal_id = request.GET.get("modal_id")
    data_id = request.GET.get("data_id")
    status = request.GET.get("status")
    value1 = str(data_id)+"-"+str(modal_id)
    
    return render(request,'open_section_based_question.html',{'value1':value1,'data_id':data_id,'status':status})






