from datetime import date, datetime
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import status
from .models import *
from .serializers import *

def _get_course_data(request):
  temp_date = request.data.get('start_date')
  start_date = temp_date.replace('"', '')
  data = {
    'title' : request.data.get('title'),
    'educator' : request.data.get('educator'),
    'start_date' : start_date,
  }

  return data

@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticatedOrReadOnly,))
def get_learner(request, pk):
  try:
    learner = Learner.objects.get(pk = pk)
  except Learner.DoesNotExist:
    return Response(status = status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = LearnerSerializer(learner)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticatedOrReadOnly,))
def get_post_learner(request):
  if request.method == 'GET':
    learner = Learner.objects.all()
    serializer = LearnerSerializer(learner, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    data = {
      'first_name' : request.data.get('first_name'),
      'last_name' : request.data.get('last_name'),
      'email' : request.data.get('email'),
    }

    serializer = LearnerSerializer(data = data)
    if serializer.is_valid():
      serializer.save()

      return Response(serializer.data, status = status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticatedOrReadOnly,))
def get_educator(request, pk):
  try:
    educator = Educator.objects.get(pk = pk)
  except Educator.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = EducatorSerializer(educator)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticatedOrReadOnly,))
def get_post_educator(request):
  if request.method == 'GET':
    educator = Educator.objects.all()
    serializer = EducatorSerializer(educator, many=True)
    return Response(serializer.data)
  
  elif request.method == 'POST':
    data = {
      'first_name' : request.data.get('first_name'),
      'last_name' : request.data.get('last_name'),
      'email' : request.data.get('email'),
    }

    serializer = EducatorSerializer(data = data)
    if serializer.is_valid():
      serializer.save()

      return Response(serializer.data, status = status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticatedOrReadOnly, ))
def get_course(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CourseSerializer(course)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticatedOrReadOnly, ))
def get_post_course(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = _get_course_data(request)
        serializer = CourseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticatedOrReadOnly, ))
def get_enrollment(request, pk):
    try:
        enrollment = Enrollment.objects.get(pk=pk)
    except Enrollment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EnrollmentSerializer(enrollment)
        return Response(serializer.data)
   
@api_view(['GET', 'POST'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticatedOrReadOnly, ))
def get_post_enrollment(request):
    if request.method == 'GET':
        enrollments = Enrollment.objects.all()
        serializer = EnrollmentSerializer(enrollments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = {
            'course': request.data.get('course'),
            'learner': request.data.get('learner'),
            'grade': request.data.get('grade'),
        }
        serializer = EnrollmentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticatedOrReadOnly, ))
def get_learners_in_course(request, pk):
    if request.method == 'GET':
        course_enrollments = Enrollment.objects.filter(course=pk)
        learners = [Learner.objects.get(pk=x.learner.pk)
                    for x in course_enrollments]
        serializer = LearnerSerializer(learners, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticatedOrReadOnly, ))
def get_courses_taken_by_learners(request, pk):
    if request.method == 'GET':
        student_enrollments = Enrollment.objects.filter(student=pk)
        courses = [Course.objects.get(pk=x.course.pk)
                   for x in student_enrollments]
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)