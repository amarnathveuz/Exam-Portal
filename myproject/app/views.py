from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import *
# Create your views here.

from django.db import IntegrityError, transaction


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

        exam_background = ""
        try:

            exam_background = request.FILES['exam_background']

        except:
            pass

        responsible_name = request.POST.get("responsible_name",False)
        
        layout = request.POST.get("layout",False)
        progression = request.POST.get("progression",False)
        exam_time_limit = request.POST.get("exam_time_limit",False)
        exam_check = request.POST.get("exam_check",False)
        if exam_check == False:
            exam_time_limit = ""
        else:
            pass
        start_message = request.POST.get("start_message",False)
        end_message = request.POST.get("end_message",False)

        selection = request.POST.get("selection_mode",False)
        Scoring = request.POST.get("Scoring",False)
        access_mode = request.POST.get("access_mode",False)

        login_required = request.POST.get("login_required",False)

        attempt_limit = request.POST.get("attempt_limit",False)
        if login_required == False:
            attempt_limit = 0
        else:
            pass

        section_line = request.POST.getlist("section_line")

        if len(section_line) == 0:
            messages.warning(request,"Add atleast one question")
            return redirect(request.META['HTTP_REFERER'])
        else:
            pass

        # Main_Exam_Master creation
        if exam_time_limit == "":
            exam_save = Main_Exam_Master.objects.create(Exam_title =exam_title,responsible_person_id =responsible_name,
            background_image = exam_background,
            start_message = start_message,end_message = end_message,
            layout = layout, progression_mode = progression,
            selection_mode = selection,
            scoring_mode = Scoring,access_mode = access_mode,
            Login_required = login_required,
            attempt_limit = attempt_limit
            )
        else:

            exam_save = Main_Exam_Master.objects.create(Exam_title =exam_title,responsible_person_id =responsible_name,
            background_image = exam_background,
            start_message = start_message,end_message = end_message,
            layout = layout, progression_mode = progression,
            Exam_time_limit = exam_time_limit,selection_mode = selection,
            scoring_mode = Scoring,access_mode = access_mode,
            Login_required = login_required,
            attempt_limit = attempt_limit
            )


        # Main_Exam_section save

        section_line_count = request.POST.getlist("section_line_count")
        modal_status = request.POST.getlist("modal_status")
       
        main_zip = zip(section_line,section_line_count,modal_status)
        for section_title,section_count,modal_status in main_zip:    

            if modal_status != "direct_question" :

                section_save = Main_Exam_section.objects.create(Exam_id_id = exam_save.id ,section_title = section_title,
                        section_type = "Section",
                        )

            else:

                section_save = Main_Exam_section.objects.create(Exam_id_id = exam_save.id ,section_title = section_title,
                        section_type = "Question",
                        )

            #  Main_Question_Bank save           

            question = request.POST.getlist("question_name"+str(section_count))
            question_description = request.POST.getlist("qstn_descriptn"+str(section_count))

            question_comment = request.POST.getlist("question_comment"+str(section_count))
            model_count = request.POST.getlist("question_model_name"+str(section_count))

            question_zip = zip(question,question_description,question_comment,model_count)
            for  question,question_description,question_comment,model_count in question_zip:

                question_type = request.POST.get("question_type"+model_count)
                question_mandatory = request.POST.get("question_mandatory"+model_count,False)

                try:
                  
                    question_image = request.FILES['question_image'+model_count]
                    question_save = Main_Question_Bank.objects.create(Question=question,
                        Description =  question_description, Question_type = question_type,
                        comments = question_comment,Imagefield =question_image,manadatory = question_mandatory)

                except:

                    question_save = Main_Question_Bank.objects.create(Question=question,
                        Description =  question_description, Question_type = question_type,
                        comments = question_comment,manadatory = question_mandatory)

                if modal_status == "direct_question":

                        section_save.Question_bank_id_id = question_save.id
                        section_save.save()

                        Section_Question_Mapping.objects.create(Section_id_id = section_save.id,Question_id_id = question_save.id)
                else:
                    Section_Question_Mapping.objects.create(Section_id_id = section_save.id,Question_id_id = question_save.id)
                    pass


                # Question_Bank_multiple_choice save 
                
                question_line_count = request.POST.getlist("question_line_count"+model_count)

                total_score = 0

                for  choice_count in question_line_count:

                    choice_data = request.POST.get("question_choice"+choice_count+'-'+model_count)
                    result_status = request.POST.get("addline_check"+choice_count+'-'+model_count,False)
                    Score = request.POST.get("Score"+choice_count+'-'+model_count,False)

                    if (result_status == "True"):
                        total_score += int(Score)

                    try:
                        file_data = request.FILES['question_image_choice'+choice_count+'-'+model_count]

                        import os
                        extension = os.path.splitext(str(file_data))[1]

                        question_choices = Question_Bank_multiple_choice.objects.create(Question_id_id=question_save.id,choice= choice_data,
                            Imagefield =  file_data, file_type = extension, Mark = Score,result_status=result_status
                            )
                        question_save.answer_id.add(question_choices.id)

                    except:

                        question_choices = Question_Bank_multiple_choice.objects.create(Question_id_id=question_save.id,choice= choice_data,
                            Mark = Score,result_status=result_status
                            )
                        question_save.answer_id.add(question_choices.id)
                        pass

                question_save.total_mark = total_score
                question_save.save()


        initial_line_count = request.POST.getlist("initial_count")

        for initial_count in initial_line_count:

            initial_label =  request.POST.get("initial_label"+initial_count)
            initial_type =  request.POST.get("initial_type"+initial_count)

            exam_initial_save = Exam_inital_field.objects.create(Exam_id_id = exam_save.id,title = initial_label,field_type = initial_type  )

            if initial_type == "selection":

                initial_answer =  request.POST.getlist("initial_answer"+initial_count)

                for i in initial_answer:

                    Exam_inital_field_choice.objects.create(initial_field_id_id = exam_initial_save.id,choice_name = i)

            else:
                pass

        messages.success(request,"Successfully added Exam details")
        return redirect('main_exam')



def open_section_based_question(request):
    modal_id = request.GET.get("modal_id")
    data_id = request.GET.get("data_id")
    status = request.GET.get("status")
    value1 = str(data_id)+"-"+str(modal_id)
    
    return render(request,'open_section_based_question.html',{'value1':value1,'modal_id':modal_id,'data_id':data_id,'status':status})


def test_lan(request):
    return render(request,'test_lan.html')





# --------------------anirudh update-----------------------------

def view_exams(request):
    exam_details = Main_Exam_Master.objects.all()
    context = {
        'exam_details' : exam_details
    }
    return render(request,'exams_view.html',context)
def exam_edit_details(request,id):
    data = Main_Exam_Master.objects.get(id=id)
    user = User.objects.all()
    data_main = Main_Exam_section.objects.filter(Exam_id_id = id)
    print("data_main:::::::::",str(data_main))
    context = {
        'data' : data,
        'user': user,
        'data_main' : data_main,
    }
    return render(request,'edit_exam_details.html',context)
def update_exam_details(request):
    updated_id = request.POST.get("updated_id",False)
    remove_status = request.POST.get("remove_status")
    exam_title = request.POST.get("exam_title",False)
    responsible_person = request.POST.get("responsible_person",False)
    start_message = request.POST.get("start_message",False)
    end_message = request.POST.get("end_message",False)
    layout = request.POST.get("layout",False)
    access_mode = request.POST.get("access_mode",False)
    progression_mode = request.POST.get("progression_mode",False)
    login_required = bool(request.POST.get('login_required', False))
    attempts_limit = request.POST.get("attempts_limit",False)
    exam_time_limit = request.POST.get("exam_time_limit",False)
    section = request.POST.get("section",False)
    scoring_mode = request.POST.get("scoring_mode",False)
    if int(remove_status) == int(1):   
        exam_background_image = request.FILES['exam_background_image']     
        remove_img = Main_Exam_Master.objects.get(id=updated_id)
        remove_img.background_image = exam_background_image
        remove_img.save()
    data_update = Main_Exam_Master.objects.filter(id=updated_id).update(
        responsible_person_id = responsible_person,
        Exam_title = exam_title,
        start_message = start_message,
        end_message = end_message,
        layout = layout,
        progression_mode = progression_mode,
        Exam_time_limit = exam_time_limit,
        selection_mode = section,
        scoring_mode = scoring_mode,
        access_mode = access_mode,
        Login_required = login_required,
        attempt_limit = attempts_limit
    )
    messages.success(request,str("Updated"))
    return redirect(request.META['HTTP_REFERER'])










def exam_title_edit_modal(request):
    data_id = request.GET.get("data_id")
    exam_data = Main_Exam_section.objects.get(id=data_id)
    return render(request,'exam_title_edit_modal.html',{'data':exam_data,'data_id':data_id})
def exam_title_edit(request):
    updated_id = request.POST.get("updated_id",False)
    exam_title = request.POST.get("exam_title")
    data=Main_Exam_section.objects.filter(id=updated_id).update(
        section_title = exam_title
        )
    messages.success(request,str("Updated"))
    return redirect(request.META['HTTP_REFERER'])
def section_Question_view_modal(request):
    data_id = request.GET.get("data_id")
    data = Main_Question_Bank.objects.get(id=data_id)
    value1 = data_id
    print(data)
    return render(request,'section_Question_view_modal.html',{'data':data,'value1':value1})
def Question_Management_update(request):
    updated_id = request.POST.get("updated_id",False)
    question_name = request.POST.get("question_name",False)
    remove_status = request.POST.get("remove_status")
    Question_type = request.POST.get("Question_type",False)
    Description = request.POST.get("Description",False)
    manadatory = bool(request.POST.get('manadatory', False))
    comments = request.POST.get("comments",False)
    choice_update = request.POST.getlist("choice_update[]",False)
    question_choice = request.POST.getlist("question_choice[]",False)
    answer = request.POST.getlist("answer[]",False)
    Score = request.POST.getlist("Score[]",False)
    data_save1=Main_Question_Bank.objects.filter(id=updated_id).update(
                Question =  question_name,
                Question_type = Question_type,
                Description = Description,
                manadatory = manadatory,
                comments =  comments
    )
    for i in range(len(choice_update)):
        print("question_choice::::::::",str(question_choice[i]))
        print("Score::::::::",Score[i])
        Question_Bank_multiple_choice.objects.filter(id=choice_update[i]).update(
                    choice = question_choice[i],
                    Mark = Score[i],
                    result_status = False
                )
        for j in range(len(answer)):
            if answer[j] == choice_update[i]:
                print("answer:qqqqqq:::::",answer[j]) 
                Question_Bank_multiple_choice.objects.filter(id=choice_update[i]).update(
                    result_status = True
                )
    messages.success(request,str("Updated"))
    return redirect(request.META['HTTP_REFERER'])





# --------------jiyad method---------------------



def attend_exam(request):
    type=request.GET.get("type")
    data = Main_Exam_Master.objects.get(id=type)
    print("data:::::::::::::::::",str(data))
    return render(request,'attend_exam.html',{'data':data})
def wizard(request):
    id = request.GET.get("type")
    data_main_exam = Main_Exam_Master.objects.get(id=id)
    # data_question = Main_Question_Bank.objects.filter(status=True)
    # print(data_question)
    data_count = ""
    print("count::::::::",str(data_main_exam.layout ))
    if (data_main_exam.layout == "0"):
        data = Section_Question_Mapping.objects.filter(Section_id__Exam_id=data_main_exam)
        print("data:::::::::::",str(data))
    elif (data_main_exam.layout == "1"):
        data = Main_Exam_section.objects.filter(Exam_id=data_main_exam)
    else:
        data = Section_Question_Mapping.objects.filter(Section_id__Exam_id=data_main_exam)
        data_count = data.count()
    return render(request, 'wizard.html', {'data_main_exam': data_main_exam, 'data': data,'data_count':data_count})
def exam_result(request):
    id = request.GET.get("type")
    total_mark = 0
    total_score = 0
    data_main_exam = Main_Exam_Master.objects.get(id=id)
    data_new = Section_Question_Mapping.objects.filter(Section_id__Exam_id=data_main_exam)
    if request.method == "POST":
        question_id = request.POST.getlist("question_id")
        for i in question_id:
            data = Main_Question_Bank.objects.get(id=i)
            if data.Question_type == "Checkbox":
                answer = request.POST.getlist("answer"+i)
                for j in answer:
                    try:
                        data_option = Question_Bank_multiple_choice.objects.get(id=j)
                        if (data_option.result_status == True):
                            total_score += data_option.Mark
                            data_create = customer_answers.objects.create(auth_user=request.user,Exam_id=data_main_exam, Question_id=data,answer=data_option.choice, Mark=data_option.Mark)
                        else:
                            data_create = customer_answers.objects.create(auth_user=request.user,Exam_id=data_main_exam, Question_id=data,
                                                                          answer=data_option.choice,
                                                                          Mark=0)
                    except:
                        pass
            else:
                answer = request.POST.get("answer"+i)
                try:
                    data_option = Question_Bank_multiple_choice.objects.get(id=answer)
                    if (data_option.result_status == True):
                        total_score += data_option.Mark
                        data_create = customer_answers.objects.create(auth_user=request.user,Exam_id=data_main_exam, Question_id=data,
                                                                      answer=data_option.choice, Mark=data_option.Mark)
                    else:
                        data_create = customer_answers.objects.create(auth_user=request.user,Exam_id=data_main_exam, Question_id=data,
                                                                      answer=data_option.choice, Mark=0)
                except:
                    pass
            total_mark += data.total_mark
    data_answer = customer_answers.objects.filter(auth_user=request.user,Exam_id=data_main_exam)
    return render(request, 'exam_result.html', {'data_new': data_new,'data_main_exam': data_main_exam,'total_mark':total_mark,'total_score':total_score,'data_answer':data_answer})



def customer_using_link(request):
    data = Exam_inital_field.objects.all()
    return render(request,'customer_using_link.html',{'data':data})