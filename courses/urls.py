from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    url(
        r'^api/learners/<pk>',
        views.get_learner,
        name='get_learner'
    ),
    url(
        r'^api/learners/$',
        views.get_post_learner,
        name='get_post_learner'
    ),
    url(
        r'^api/educators/(?P<pk>[0-9]+)$',
        views.get_educator,
        name='get_educator'
    ),
    url(
        r'^api/educators/$',
        views.get_post_educator,
        name='get_post_educator'
    ),
    url(
        r'^api/courses/(?P<pk>[0-9]+)$',
        views.get_course,
        name='get_course'
    ),
    url(
        r'^api/courses/$',
        views.get_post_course,
        name='get_post_course'
    ),
    url(
        r'^api/enrollments/(?P<pk>[0-9]+)$',
        views.get_enrollment,
        name='get_enrollment'
    ),
    url(
        r'^api/enrollments/$',
        views.get_post_enrollment,
        name='get_post_enrollment'
    ),
    url(
        r'^api/learner/:course_id/(?P<pk>[0-9]+)$',
        views.get_learners_in_course,
        name='get_learners_in_course'
    ),    
    url(
        r'^api/courses/:student_id/(?P<pk>[0-9]+)$',
        views.get_courses_taken_by_learners,
        name='get_courses_taken_by_learners'
    ),
    
]