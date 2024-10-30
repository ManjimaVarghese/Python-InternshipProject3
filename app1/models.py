





from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone

#/////////////////////////////////models for hod///////////////////////////////////////////////////

from django.contrib.auth.models import User

class department(models.Model):
    department_name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.department_name



class staffreg(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    staff_name = models.CharField(max_length=200)
    department = models.ForeignKey(department, on_delete=models.CASCADE)
    designation = models.CharField(max_length=50, null=True)
    mobile = models.IntegerField(null=True)
    saved_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.staff_name

   



class studentreg(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
     student_name = models.CharField(max_length=200)
     department = models.ForeignKey(department, on_delete=models.CASCADE)
     gender = models.CharField(max_length=10, null=True)
     birth_date = models.DateField(null=True)
     mobile = models.IntegerField(null=True)
     saved_time = models.DateTimeField(default=timezone.now)


     def __str__(self):
        return self.student_name






class syllabusupload(models.Model):
    department=models.ForeignKey(department, on_delete=models.CASCADE)
    syllabus_Upload = models.ImageField(upload_to='profile',default="")
    subject_hours= models.IntegerField(null = True)

class events(models.Model):
    event_name =  models.CharField(max_length = 200)
    event_startdate = models.DateField(null = True)
    event_enddate = models.DateField(null = True)
    location =  models.CharField(max_length = 200)
    Staff_Incharge =  models.CharField(max_length = 200)


class replaystaffleav(models.Model):
    staff = models.ForeignKey(staffreg, on_delete=models.CASCADE)
    
    
    STATUS_CHOICES = (
        
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES)




class replaystudleav(models.Model):
    student = models.ForeignKey(studentreg, on_delete=models.CASCADE)
    
    STATUS_CHOICES = (
        
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES)




class Qpaperupload(models.Model):
    department=models.ForeignKey(department, on_delete=models.CASCADE)
    qpaper_Upload = models.ImageField(upload_to='profile',default="")
    duration= models.IntegerField(null = True)







#/////////////////////////////////models for student///////////////////////////////////////////////////





class stud_feedback(models.Model):
    
    feedback = models.TextField(max_length = 200)

class stud_applyleave(models.Model):
  
    reason = models.TextField(max_length = 200)
    start_date = models.DateField()
    end_date = models.DateField()



class uploadanswer(models.Model):
    department=models.ForeignKey(department, on_delete=models.CASCADE,default=None)
    student = models.ForeignKey(studentreg, on_delete=models.CASCADE,default=None)
    answersheet = models.ImageField(upload_to='profile',default="")


    

#/////////////////////////////////models for staff///////////////////////////////////////////////////



class markattendance(models.Model):
    
    student = models.ForeignKey(studentreg, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField(default=False)



class addgrade(models.Model):
    student = models.ForeignKey(studentreg, on_delete=models.CASCADE)
    grade =  models.CharField(max_length = 200)



class  staffapplyleave(models.Model):
    staff = models.ForeignKey(studentreg, on_delete=models.CASCADE,null=True)
    reason = models.TextField(max_length = 200)
    start_date = models.DateField()
    end_date = models.DateField()

class staff_feedback(models.Model):
    
    feedback = models.TextField(max_length = 200)


class uploadmark(models.Model):
    department=models.ForeignKey(department, on_delete=models.CASCADE,default=None)
    student = models.ForeignKey(studentreg, on_delete=models.CASCADE,default=None)
    mark = models.IntegerField(null=True)


#/////////////////////////////////models for placement///////////////////////////////////////////////////
    

class companies(models.Model):
    company_name = models.CharField(max_length = 200)
    location = models.CharField(max_length = 200)
    industry = models.CharField(max_length = 200 ,default='')
    
    
   

    def __str__(self):
        return self.company_name



class allocatestudent(models.Model):
    company_name = models.ForeignKey(companies, on_delete=models.CASCADE)
    student_name = models.ForeignKey(studentreg, on_delete=models.CASCADE)
    department_name=models.ForeignKey(department, on_delete=models.CASCADE,default='')
    salary =  models.CharField(max_length = 200,default='')
    student_image = models.ImageField(null=True,blank=True,upload_to="profile/")
    

    
    def _str_(self):
        return f"{self.student_name} - {self.company_name} - {self.department_name}"


class placementcontact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(
        max_length=254,  
        unique=True,     
        blank=False,     
        help_text='Please enter a valid email address.' 
    )
    message = models.TextField(max_length = 200)

    def _str_(self):
        return self.name



class replaying_for_contact(models.Model):

    student = models.ForeignKey(studentreg, on_delete=models.CASCADE)
    replay_message = models.TextField(max_length = 200)



#/////////////////////////////////models for fee///////////////////////////////////////////////////
    

class feemanagement(models.Model):
    department_name=models.ForeignKey(department, on_delete=models.CASCADE,default='')
    student_name = models.ForeignKey(studentreg, on_delete=models.CASCADE)
    year = models.IntegerField(default='')
    fees = models.IntegerField(default='')