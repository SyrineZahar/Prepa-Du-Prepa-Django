from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from PrepaDuPrepa.models import user,course
from PrepaDuPrepa.serializers import UserSerializer,CourseSerializer  

@csrf_exempt
def usersApi(request, id=0):
    if request.method == 'GET':
        if id != 0:
            user_instance = user.objects.filter(userId=id).first()
            if user_instance:
                users_serializer = UserSerializer(user_instance)
                return JsonResponse(users_serializer.data, safe=False)
            else:
                return JsonResponse("Utilisateur non trouvé", safe=False)
        else:
            users = user.objects.all()
            users_serializer = UserSerializer(users, many=True)
            return JsonResponse(users_serializer.data, safe=False)

    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        users_serializer = UserSerializer(data=user_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("ajout avec succes", safe=False)
        return JsonResponse("ajout échoué", safe=False)

    elif request.method == 'PUT':
        user_data = JSONParser().parse(request)
        user_instance = user.objects.get(userId=user_data['userId'])
        users_serializer = UserSerializer(user_instance, data=user_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("modification avec succes", safe=False)
        return JsonResponse("modification échoué", safe=False)

    elif request.method == "DELETE":
        user_instance = user.objects.get(userId=id)
        user_instance.delete()
        return JsonResponse("suppression avec succes", safe=False)







@csrf_exempt
def coursesApi(request, id=0):
    if request.method == 'GET':
        if id != 0:
            course_instance = course.objects.filter(courseId=id).first()
            if course_instance:
                course_serializer = CourseSerializer(course_instance)
                return JsonResponse(course_serializer.data, safe=False)
            else:
                return JsonResponse("Utilisateur non trouvé", safe=False)
        else:
            courses = course.objects.all()
            course_serializer = CourseSerializer(courses, many=True)
            return JsonResponse(course_serializer.data, safe=False)

    elif request.method == 'POST':
        course_data = JSONParser().parse(request)
        course_serializer = CourseSerializer(data=course_data)
        if course_serializer.is_valid():
            course_serializer.save()
            return JsonResponse("ajout avec succes", safe=False)
        return JsonResponse("ajout échoué", safe=False)

    elif request.method == 'PUT':
        course_data = JSONParser().parse(request)
        course_instance = course.objects.get(courseId=course_data['courseId'])
        course_serializer = CourseSerializer(course_instance, data=course_data)
        if course_serializer.is_valid():
            course_serializer.save()
            return JsonResponse("modification avec succes", safe=False)
        return JsonResponse("modification échoué", safe=False)

    elif request.method == "DELETE":
        course_instance = course.objects.get(courseId=id)
        course_instance.delete()
        return JsonResponse("suppression avec succes", safe=False)