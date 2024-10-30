
from django.urls import path
from .import views 
from .views import AttandanceView,StaffFeedbackView,ApplyLeaveView,StaffLeavApply

  
urlpatterns = [ 
    path('',views.index,name='index'),
    path('staff/',views.staff,name='staff'), 
     path('staffupmark/',views.staffupmark,name='staffupmark'),
      path('studvmark/',views.studvmark,name='studvmark'),
    path('staffvsyllabus/',views.staffvsyllabus,name='staffvsyllabus'), 
    path('studvsyllabus/',views.studvsyllabus,name='studvsyllabus'), 
    path('studvqs/',views.studvqs,name='studvqs'),
    path('staffvqs/',views.staffvqs,name='staffvqs'),
    path('staffvansr/',views.staffvansr,name='staffvansr'),
    path('stafflogin/',views.stafflogin,name='stafflogin'),
    path('studlogin/',views.studlogin,name='studlogin'),
    path('staff_changepassword/',views.staff_changepassword,name='staff_changepassword'),
    path('students/',views.students,name='students'),
    path('studviewgrade/',views.studviewgrade,name='studviewgrade'),
    path('staffsignout/',views.staffsignout,name='staffsignout'),
    path('studsignout/',views.studsignout,name='studsignout'),
    path('syllabus/',views.syllabus,name='syllabus'),
    path('studuploadans/',views.studuploadans,name='studuploadans'),
    path('events/',views.events,name='events'),
    path('feelogin/',views.feelogin,name='feelogin'),
    path('stud_feedback/',views.submitfeedback,name='stud_feedback'), 
    path('applyleave/', ApplyLeaveView.as_view(), name='apply_leave'), 
    path('attmarking/',AttandanceView.as_view(),name='attmarking'), 
    path('staff_upgrade/',views.staff_upgrade,name='staff_upgrade'),
    path('staffpage/',views.staffpage,name='staffpage'),
    path('staff_feedback/',StaffFeedbackView.as_view(),name='staff_feedback'),
    path('studpage/',views.studpage,name='studpage'),
    path('staffleavapply/',StaffLeavApply.as_view(),name='staffleavapply'),
    path('stafflogin/',views.stafflogin,name='stafflogin'),
    path('studviewevents/',views.studviewevents,name='studviewevents'),
    path('staffvstatus/',views.staffvstatus,name='staffvstatus'),
    path('studvstatus/',views.studvstatus,name='studvstatus'),
    path('placements/',views.placements,name='placements'), 



    path('create_company/', views.create_company, name='create_company'),
    path('showcompanies/',views.show_companies,name='showcompanies'),
    path('company_update/<int:pk>/',views.company_update,name='company_update'),
    path('company_delete/<int:pk>/',views.company_delete,name='company_delete'),



    path('add_student/', views.add_student, name='add_student'),
    path('showstudents/',views.show_students,name='showstudents'),
    path('student_update/<int:pk>/',views.student_update,name='student_update'),
    path('student_delete/<int:pk>/',views.student_delete,name='student_delete'),



    path('placementhome/',views.placementhome,name='placementhome'),


    
    path('placementcontact/',views.contact_placement_cell,name='placementcontact'),


    path('studentfee/', views.studentfee,name='studentfee'),
    path('showfees/', views.showfees,name='showfees'),
    path('feesupdate/<int:pk>/',views.feesupdate,name='feesupdate'),
    path('studentfeedelete/<int:pk>/',views.studentfeedelete,name='studentfeedelete'),



    path('studentfeemanagement/',views.studentfeemanagement,name = 'studentfeemanagement'),

     path('checkout/<int:product_id>/',views.checkout,name = 'checkout'),


    path('feeofficerlogin/',views.feeofficerlogin,name='feeofficerlogin'),
    path('placementofficerlogin/',views.placementofficerlogin,name='placementofficerlogin'),
    path('feeofficerlogout/',views.feeofficerlogout,name='feeofficerlogout'),
    path('placementofficerlogout/',views.placementofficerlogout,name='placementofficerlogout'),


    
    
    
    
  
]