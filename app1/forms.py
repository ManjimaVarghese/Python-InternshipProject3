

from .models import stud_feedback,studentreg,stud_applyleave,markattendance,addgrade
from . models import staffreg,staffapplyleave,staff_feedback
from django import forms
    

class stud_feedback(forms.ModelForm):
   

        

    feedback = forms.Textarea(attrs={'class': 'form-control'})
    


    class Meta:
        model = stud_feedback
        fields = [ 'feedback']





class stud_applyleave(forms.ModelForm):
   
    date_choices = [(year, str(year)) for year in range(2022, 2030)] 
    reason = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    start_date = forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'form-control'}), initial={'year': 2022, 'month': 1, 'day': 1},)
    end_date = forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'form-control'}), initial={'year': 2022, 'month': 1, 'day': 1},)
    class Meta:
        model = stud_applyleave
        fields = ['reason', 'start_date', 'end_date']

     # Customize the range as needed








# forms.py
from django import forms
from .models import markattendance, studentreg

 # Assuming you have a model named MarkAttendance

class MarkAttendanceForm(forms.Form):
    def __init__(self, students, today_date, *args, **kwargs):
        super(MarkAttendanceForm, self).__init__(*args, **kwargs)

        for student in students:
            attendance_instance = markattendance.objects.filter(student=student, date=today_date).first()
            is_present_initial = attendance_instance.is_present if attendance_instance else False

            self.fields[f"student_{student.id}"] = forms.BooleanField(
                label=student.name,
                required=False,
                initial=is_present_initial,
                widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
            )


class addgrade(forms.ModelForm):
    student = forms.ModelChoiceField(
        queryset=studentreg.objects.all(),
        empty_label=None,
        label='Select Student',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    GRADE_CHOICES = [('P', 'P'), ('F', 'F')]
    
    grade = forms.ChoiceField(choices=GRADE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    class Meta:
        model = addgrade
        fields = ['student', 'grade']



from django import forms
from .models import staffreg

class staffapplyleave(forms.ModelForm):

    date_choices = [(year, str(year)) for year in range(2022, 2030)] 
    reason = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    start_date = forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'form-control'}), initial={'year': 2022, 'month': 1, 'day': 1},)
    end_date = forms.DateField(widget=forms.SelectDateWidget(attrs={'class': 'form-control'}), initial={'year': 2022, 'month': 1, 'day': 1},)
    
    class Meta:
        model = staffapplyleave  # Provide the model class, not an instance
        fields = ['reason', 'start_date', 'end_date']


















class stafffeedback(forms.ModelForm):
   

        

   
 
    feedback = forms.Textarea(attrs={'class': 'form-control'})
    


    class Meta:
        model = staff_feedback
        fields = [ 'feedback']





from .models import companies,allocatestudent,placementcontact,feemanagement


class CompaniesForm(forms.ModelForm):
    class Meta:
        model = companies
        fields = ['company_name', 'location','industry']


class StudentForm(forms.ModelForm):
    class Meta:
        model = allocatestudent
        fields = ['company_name', 'student_name','department_name','salary','student_image']


class PlacementContactForm(forms.ModelForm):
    class Meta:
        model = placementcontact
        fields = ['name', 'email','message']



class FeeManagementForm(forms.ModelForm):
    class Meta:
        model =feemanagement
        fields = ['department_name', 'student_name','year','fees']












from .models import uploadanswer

class studuploadanswer(forms.ModelForm):

   
  
    class Meta:
        model = uploadanswer
        fields = ['answersheet','department','student']

from .models import uploadmark

class staffuploadmark(forms.ModelForm):

   
  
    class Meta:
        model = uploadmark
        fields = ['department','student','mark']