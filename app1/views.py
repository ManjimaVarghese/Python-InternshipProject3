from django.shortcuts import render,redirect,get_object_or_404


from .models import markattendance, studentreg,addgrade,events
from datetime import date
from django .views import View
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, logout

from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from .forms import stud_feedback,stud_applyleave,addgrade,staffapplyleave,stafffeedback
from .forms import markattendance,staff_feedback
# Create your views here.
def index(request):
    return render(request,'index.html')

from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required




    

    # if request.session.get('id'):
    #    id=request.session.get('id')

def stafflogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            staff_instance = staffreg.objects.get(user=user)
            # Store the student's ID in the session
          
            request.session['id'] = staff_instance.id
           
            return redirect('staffpage')  # Redirect to the staff page
        else:
            return render(request, 'stafflogin.html')
    else:
        return render(request, 'stafflogin.html')


def staffpage(request):
    if request.session.get('id'):
         return render(request,'staffpage.html')
    else:
        return render(request, 'stafflogin.html')


def staffsignout(request):
    if 'username' in request.session:
        del request.session['username']
    
    logout(request)
    return redirect('stafflogin')






from django.contrib.auth.forms import PasswordChangeForm

def staff_changepassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect(stafflogin)
        else:
            return render(request,'staff_changepassword.html',{'form':form})          
    else:
        form = PasswordChangeForm(request.user)
        return render(request,'staff_changepassword.html',{'form':form})
    

def studlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')  # Assuming you have a password field in your form
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            student_instance = studentreg.objects.get(user=user)
            # Store the student's ID in the session
            request.session['sid'] = student_instance.id
            # request.session['sid'] = user.id
           
            return redirect('studpage') 
        else:
        # Handle GET request (display login page)
            return render(request, 'studlogin.html')
    else:
        return render(request, 'studlogin.html')
  
    



def studpage(request):
     if request.session.get('sid'):
         return render(request,'studpage.html')
     else:
         return render(request, 'studlogin.html')

def studsignout(request):
    if 'sid' in request.session:
        del request.session['sid']
    
    logout(request)
    return redirect('studlogin')








def staff(request):
    return render(request,'staff.html')
def students(request):
    return render(request,'students.html')
def syllabus(request):
    return render(request,'syllabus.html')
def events(request):
    return render(request,'events.html')


def feepage(request):
    return render(request,'feepage.html')

    



class StaffFeedbackView(View):
    def get(self, request):
        form = stafffeedback()
        return render(request, 'staff_feedback.html', {'form': form})

    def post(self, request):
        form = stafffeedback(request.POST, request.FILES)
        if form.is_valid():
            
            feedback = form.cleaned_data['feedback']
            form.save()
           
            form.instance.feedback = feedback
            msg = 'Staff feedback inserted successfully'
            return render(request, 'staff_feedback.html', {'msg': msg, 'form': form})
        else:
            return render(request, 'staff_feedback.html', {'form': form})






def submitfeedback(request):
    if request.method == 'POST':
        form = stud_feedback(request.POST,request.FILES)

        if form.is_valid():
            
          
            feedback = form.cleaned_data['feedback']
            
            form.save()
           
           
            form.instance.feedback = feedback
            
            msg = 'student feedback inserted successfully'
            return render(request, 'stud_feedback.html', {'msg': msg,'form': form})
    else:
        form = stud_feedback()
    return render(request, 'stud_feedback.html', {'form': form})






class ApplyLeaveView(View):
    def get(self, request):
        form = stud_applyleave()
        return render(request, 'applyleave.html', {'form': form})

    def post(self, request):
        form = stud_applyleave(request.POST, request.FILES)
        if form.is_valid():
            
            reason = form.cleaned_data['reason']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            
            form.save()
            
            form.instance.reason = reason
            form.instance.start_date = start_date
            form.instance.end_date = end_date

            msg = 'Leave request sent successfully'
            return render(request, 'applyleave.html', {'msg': msg, 'form': form})
        else:
            return render(request, 'applyleave.html', {'form': form})
        
class StaffLeavApply(View):
    def get(self, request):
        form = staffapplyleave()
        return render(request, 'staffleavapply.html', {'form': form})

    def post(self, request):
        form = staffapplyleave(request.POST, request.FILES)
        if form.is_valid():
            
            reason = form.cleaned_data['reason']
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            
            instance = form.save(commit=False)
         
            instance.reason = reason
            instance.start_date = start_date
            instance.end_date = end_date
            instance.save()

            msg = 'Leave request sent successfully'
            return render(request, 'staffleavapply.html', {'msg': msg, 'form': form})
        else:
            return render(request, 'staffleavapply.html', {'form': form})










from datetime import date
from django.shortcuts import render
from .models import markattendance, studentreg

from django.shortcuts import render
from .models import studentreg, markattendance,staffreg
from datetime import date
class AttandanceView(View):
 def get(self, request):
        staff_id = request.session.get('id')
        staff_instance = staffreg.objects.get(id=staff_id)
        students = studentreg.objects.filter(department_id=staff_instance.department_id)
        today_date = date.today()
        return render(request, 'attmarking.html', {'students': students, 'today_date': today_date})

 def post(self, request):
    staff_id = request.session.get('id')
    staff_instance = staffreg.objects.get(id=staff_id)
    students = studentreg.objects.filter(department=staff_instance.department)
    today_date = date.today()
    for student in students:
        is_present_str = request.POST.get(f"student_{student.id}", "False")
        is_present = is_present_str == "True"

        # Check if the checkbox is checked, and update the attendance only if it has changed
        attendance_instance, created = markattendance.objects.get_or_create(
            student=student,
            date=today_date,
            defaults={'is_present': is_present}
        )
        if not created and attendance_instance.is_present != is_present:
            attendance_instance.is_present = is_present
            attendance_instance.save()

    msg = 'Attendance recorded successfully'
    return render(request, 'attmarking.html', {'students': students, 'today_date': today_date, 'msg': msg})

from .models import syllabusupload
def staffvsyllabus(request):
   staff_id = request.session.get('id')
   staff_instance = staffreg.objects.get(id=staff_id)
   datas = syllabusupload.objects.filter(department_id=staff_instance.department_id)
   return render(request, 'staffvsyllabus.html', {'datas': datas})
def studvsyllabus(request):
   student_id = request.session.get('sid')
   print('student_id')
   stud_instance = studentreg.objects.get(id=student_id)
   datas = syllabusupload.objects.filter(department_id=stud_instance.department_id)
   return render(request, 'staffvsyllabus.html', {'datas': datas})
from .forms import addgrade      
def staff_upgrade(request):
    if request.method == 'POST':
        form = addgrade(request.POST, request.FILES)  # Create an instance of your form class

        if form.is_valid():  # Validate the form data
            student = form.cleaned_data['student']
            grade = form.cleaned_data['grade']
            form.instance.student = student
            form.instance.grade = grade
            form.save()  # Save the form data
            msg = 'Message sent successfully'
            return render(request, 'staff_upgrade.html', {'msg': msg, 'form': form})
    else:
        form = addgrade()  # Create an empty form instance

    return render(request, 'staff_upgrade.html', {'form': form})


from .models import Qpaperupload,uploadanswer,uploadmark
def studvqs(request):
   student_id = request.session.get('sid')
   print('student_id')
   stud_instance = studentreg.objects.get(id=student_id)
   datas = Qpaperupload.objects.filter(department_id=stud_instance.department_id)
   return render(request, 'studvqs.html', {'datas': datas})

def staffvansr(request):
   staff_id = request.session.get('id')
  
   staff_instance = staffreg.objects.get(id=staff_id)
   datas = uploadanswer.objects.filter(department_id=staff_instance.department_id)
   return render(request, 'staffvansr.html', {'datas': datas})

def studvmark(request):
   student_id = request.session.get('sid')
  
   stud_instance = studentreg.objects.get(id=student_id)
   datas = uploadmark.objects.filter(department_id=stud_instance.department_id)
   return render(request, 'studvmark.html', {'datas': datas})


from .forms import studuploadanswer
def studuploadans(request):
    if request.method == 'POST':
        form = studuploadanswer(request.POST,request.FILES)

        if form.is_valid():
            department = form.cleaned_data['department']
            student = form.cleaned_data['student']
            answersheet = form.cleaned_data['answersheet']
            
            form.save()
           
           
            form.instance.department = department
            form.instance.student = student
            form.instance.answersheet = answersheet
          
            msg = 'uploaded'
            return render(request, 'studuploadans.html', {'msg': msg,'form': form})
    else:
        form = studuploadanswer()
    return render(request, 'studuploadans.html', {'form': form})


from .forms import staffuploadmark
def staffupmark(request):
    if request.method == 'POST':
        form = staffuploadmark(request.POST,request.FILES)

        if form.is_valid():
            
            department = form.cleaned_data['department']
            student = form.cleaned_data['student']
            mark = form.cleaned_data['mark']
            
            form.save()
           
            
            form.instance.department = department
            form.instance.student = student
            form.instance.mark = mark
          
            msg = 'uploaded'
            return render(request, 'staffupmark.html', {'msg': msg,'form': form})
    else:
        form = staffuploadmark()
    return render(request, 'staffupmark.html', {'form': form})




#////////////////////////view section///////////////


from .models import addgrade
def studviewgrade(request):
    datas=addgrade.objects.all()
    return render(request,'studviewgrade.html',{'datas':datas})
from .models import events
def studviewevents(request):
    datas=events.objects.all()
    return render(request,'studviewevents.html',{'datas':datas})
from .models import Qpaperupload
def staffvqs(request):
    staff_id = request.session.get('id')
    staff_instance = staffreg.objects.get(id=staff_id)
    datas = Qpaperupload.objects.filter(department_id=staff_instance.department_id)
    
    return render(request,'staffvqs.html',{'datas':datas})
from .models import replaystaffleav
def staffvstatus(request):


    
    user_id = request.session.get('sid')

    print(user_id)
    
    # datas = replaystudleav.objects.filter(user_id=request.user.id).get()
    try:

        datas=replaystaffleav.objects.get(id=user_id)
        dt=datas.status
    except Exception as e:
        print(e)
        dt='not status updated'
    
    return render(request,'staffvstatus.html',{'datas':dt})



    
    

from .models import replaystudleav
def studvstatus(request):
 
    user_id = request.session.get('sid')

    print(user_id)
    
    # datas = replaystudleav.objects.filter(user_id=request.user.id).get()
    try:

        datas=replaystudleav.objects.get(id=user_id)
        dt=datas.status
    except Exception as e:
        print(e)
        dt='not status updated'
    
    return render(request,'studvstatus.html',{'datas':dt})










from django.shortcuts import get_object_or_404, render, redirect
from .forms import CompaniesForm,StudentForm,PlacementContactForm,FeeManagementForm
from .models import companies,allocatestudent,feemanagement


def placements(request):
    stud = allocatestudent.objects.all()
    return render(request,'placements.html' ,{'stud': stud})





def create_company(request):
    if request.method == 'POST':
        form = CompaniesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showcompanies')  
    else:
        form = CompaniesForm()

    return render(request, 'company.html', {'form': form})


def show_companies(request):
    data = companies.objects.all()
    return render(request,'show_companies.html' ,{'data': data})



def company_update(request,pk):
    data = get_object_or_404(companies, pk = pk)
    if request.method == 'POST':
        form = CompaniesForm(request.POST,instance=data)
        if form.is_valid:
            form.save()
        return redirect('showcompanies')
    else:
        form = CompaniesForm(instance=data)
    return render(request, 'company_update.html', {'form': form, 'data': data})



def company_delete(request, pk):
    data = get_object_or_404(companies, pk=pk)
    if request.method == 'POST':
        data.delete()
        return redirect('showcompanies')
    return render(request, 'company_delete.html', {'data': data})












def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('showstudents')  
    else:
        form = StudentForm()

    return render(request, 'studentsadd.html', {'form': form})




def show_students(request):
    data = allocatestudent.objects.all()
    return render(request,'show_students.html' ,{'data': data})





def student_update(request,pk):
    data = get_object_or_404(allocatestudent, pk = pk)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=data)
        if form.is_valid:
            form.save()
        return redirect('showstudents')
    else:
        form = StudentForm(instance=data)
    return render(request, 'student_update.html', {'form': form, 'data': data})




def student_delete(request, pk):
    data = get_object_or_404(allocatestudent, pk=pk)
    if request.method == 'POST':
        data.delete()
        return redirect('showstudents')
    return render(request, 'student_delete.html', {'data': data})



def placementhome(request):
    return render(request,'placementhome.html')

def contact(request):
    return render(request,'contact.html')


def contact_placement_cell(request):
    if request.method == 'POST':
        form = PlacementContactForm(request.POST)
        if form.is_valid():
            form.save()
            # You may add further logic like sending emails or redirecting to a thank-you page
            return redirect('placements')
    else:
        form = PlacementContactForm()

    return render(request, 'contact.html', {'form': form})




def studentfee(request):
    if request.method == 'POST':
        form = FeeManagementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showfees')  
    else:
        form = FeeManagementForm()

    return render(request, 'studentfees.html', {'form': form})





def showfees(request):
    data = feemanagement.objects.all()
    return render(request,'showfees.html' ,{'data': data})





def feesupdate(request,pk):
    data = get_object_or_404(feemanagement, pk = pk)
    if request.method == 'POST':
        form = FeeManagementForm(request.POST,instance=data)
        if form.is_valid:
            form.save()
        return redirect('showfees')
    else:
        form = FeeManagementForm(instance=data)
    return render(request, 'feesupdate.html', {'form': form, 'data': data})



def studentfeedelete(request, pk):
    data = get_object_or_404(feemanagement, pk=pk)
    if request.method == 'POST':
        data.delete()
        return redirect('showfees')
    return render(request, 'studentfeedelete.html', {'data': data})


def studentfeemanagement(request):
    details = feemanagement.objects.all().order_by('department_name__department_name', 'year')
    return render(request, 'studentfeemanagement.html', {'details': details})




def checkout(request, product_id):
   
   
    students = feemanagement.objects.get(id = product_id)
    context = {
        'students':students,
    }
    return render(request,'checkout.html',context)









from django.contrib.auth import authenticate, login
from django.shortcuts import render

def feelogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Check if the submitted username and password match the default values
        if username == 'fee' and password == 'fee123':
            # Authenticate the user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page or return a success message
                return render(request, 'studentfeemanagement.html')
            else:
                # Handle invalid credentials
                return render(request, 'feelogin.html', {'error_message': 'Invalid username or password.'})
        else:
            # Handle incorrect default credentials
            return render(request, 'feelogin.html', {'error_message': 'Incorrect default credentials.'})
    else:
        return render(request, 'feelogin.html')
    

from django.shortcuts import render, redirect

def feeofficerlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if username and password match your criteria
        if username == 'officer' and password == 'officer123':
            # Redirect to feemanagement.html upon successful login
            return redirect('showfees')
        else:
            # Display an error message or handle invalid login
            error_message = "Incorrect username or password. Please try again."
            return render(request, 'feeofficerlogin.html', {'error_message': error_message})
    else:
        return render(request, 'feeofficerlogin.html')
    


def placementofficerlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if username and password match your criteria
        if username == 'officer' and password == 'officer123':
            # Redirect to feemanagement.html upon successful login
            return redirect('showcompanies')
        else:
            # Display an error message or handle invalid login
            error_message = "Incorrect username or password. Please try again."
            return render(request, 'placementofficerlogin.html', {'error_message': error_message})
    else:
        return render(request, 'placementofficerlogin.html')
    


def placementofficerlogout(request):
    return redirect('placements')

def feeofficerlogout(request):
    return redirect('index')