from django.urls import path
from.views import *


urlpatterns = [
     path('', landing_page, name='landing_page'),
    path('landing_page_after_login', landing_page_after_login, name='landing_page_after_login'),
    path('login_page', login_page, name='login_page'),
    path('student_signup_page', student_signup_page, name='student_signup_page'),
    path('course', course, name='course'),
    path('course_after_login', course_after_login, name='course_after_login'),
    path('roadmap_after_pg', roadmap_after_pg, name='roadmap_after_pg'),
    path('roadmap_after_pg_in_comm', roadmap_after_pg_in_comm, name='roadmap_after_pg_in_comm'),
    path('roadmap_after_pg_in_elec', roadmap_after_pg_in_elec, name='roadmap_after_pg_in_elec'),
    path('roadmap_after_pg_in_hm', roadmap_after_pg_in_hm, name='roadmap_after_pg_in_hm'),
    path('notes', notes, name='notes'),
    path('download_pdf', download_pdf, name='download_pdf'),
    path('module', module, name='module'),
    path('my_course', my_course, name='my_course'),
    path('course_material', course_material, name='course_material'),
    path('payment', payment, name='payment'),
     path('reply_to_post', reply_to_post, name='reply_to_post'),
     path('course_video', course_video, name='course_video'),
     path('course_overview', course_overview, name='course_overview'),
     path('quiz_page', quiz_page, name='quiz_page'),
     path('assignment_page', assignment_page, name='assignment_page'),
     path('quiz_questions', quiz_questions, name='quiz_questions'),
     path('assessment_questions', assessment_questions, name='assessment_questions'),
     path('result', result, name='result'),
     path('quiz_result', quiz_result, name='quiz_result'),
     path('assessment_result', assessment_result, name='assessment_result'),
     path('certificate', certificate, name='certificate'),
     path('ticket', ticket, name='ticket'),
     path('referral', referral, name='referral'),
      path('payment_history', payment_history, name='payment_history'),
      path('profile_page', profile_page, name='profile_page'),
     path('e_learning_plus', e_learning_plus, name='e_learning_plus'),
     path('referral_progress', referral_progress, name='referral_progress'),
     path('tech_courses', tech_courses, name='tech_courses'),
     path('ncert_courses', ncert_courses, name='ncert_courses'),
     path('question_papers', question_papers, name='question_papers'),
     path('grade_wise_courses', grade_wise_courses, name='grade_wise_courses'),
     path('roadmap', roadmap, name='roadmap'),
     path('blog_details', blog_details, name='blog_details'),
     path('blog', blog, name='blog'),
    path('login',do_login,name='login'),
    path('student-signup/',student_signup,name='student-signup'),
    path('verify-otp',verify_otp,name='verify_otp'),
    path('logout/', logout_user, name='logout'),

    path('course_catalog', course_catalog, name='course_catalog'),
    path('career_roadmap', career_roadmap, name='career_roadmap'),

    path('mentorship_page/', homepage, name='mentorship_page'),
    path('paymenthandler/', paymenthandler, name='paymenthandler'),
    path('course/<int:course_id>/', view_course_details, name='view_course_details'),
    path('enroll-course/<int:course_id>/', enroll_course, name='enroll_course'),
    path('course_payment/<int:course_id>/', course_payment, name='course_payment'),
    path('enrolled-courses/', enrolled_course, name='enrolled_course'),
    path('enrolled-courses/<int:course_id>/start-course', start_course, name='start_course'),
    path('start-course/<int:course_id>/previous_question_papers/', previous_question_papers,
         name='previous_question_papers'),

    path('community/',community_platform, name='community_platform'),
    path('community/add_post/',add_post, name='add_post'),
    path('community/add_comment/<int:post_id>/',add_comment, name='add_comment'),

    path('like_post/<int:post_id>/',like_post, name='like_post'),
    path('dislike_post/<int:post_id>/',dislike_post, name='dislike_post'),
    path('like_comment/<int:comment_id>/', like_comment, name='like_comment'),
    path('dislike_comment/<int:comment_id>/', dislike_comment, name='dislike_comment'),

]