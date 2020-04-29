import json

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from bear import models
from bear.forms import UserForm, ResetForm
# from bear.response import ResponseData


def index(request):
    return render(request, 'login.html')


def logout(request):
    if request.method == "POST":
        if request.session.get('is_login', None):
            request.session.flush()
            return redirect('/bear/')


def reset(request):
    return render(request, 'reset_pwd.html')


def reset_pwd(request):
    if request.method == "POST":
        reset_form = ResetForm(request.POST)
        if reset_form.is_valid():
            account = reset_form.cleaned_data['account']
            password = reset_form.cleaned_data['password']
            question_id = reset_form.cleaned_data['question_id']
            answer = reset_form.cleaned_data['answer']
            usertype = reset_form.cleaned_data['usertype']
            try:

                if usertype == 1:
                    user = models.Stu_info.objects.get(studentNo=account, questionNo=question_id)
                    if user.answer == answer:
                        models.Stu_info.objects.filter(studentNo=account).update(stuPassword=password)
                        return HttpResponse(content="密码修改成功")
                    else:
                        return HttpResponse(content="问题错误")
                elif usertype == 2:
                    user = models.Tec_info.objects.get(teacherNo=account, questionNo=question_id)
                    if user.answer == answer:
                        models.Tec_info.objects.filter(teacherNo=account).update(tecPassword=password)
                        return HttpResponse(content="密码修改成功")
                    else:
                        return HttpResponse(content="问题错误")
            except Exception as e:
                print(e)
                return HttpResponse(content="密码修改失败")


def login(request):
    if request.session.get('is_login', None):
        No = request.session.get('user_id', None),

        return render(request, 'student.html', locals())

    if request.method == "POST":
        login_form = UserForm(request.POST)

        if login_form.is_valid():  # 确保用户名和密码都不为空
            account = login_form.cleaned_data['account']
            password = login_form.cleaned_data['password']
            usertype = login_form.cleaned_data['usertype']

            try:
                if usertype is 1:

                    user = models.Stu_info.objects.get(studentNo=account)
                    if user.stuPassword == password:
                        request.session['is_login'] = True
                        request.session['user_id'] = account

                        No = account

                        return render(request, 'student.html', locals())
                    else:
                        message = "密码不正确！"

                elif usertype is 2:
                    user = models.Tec_info.objects.get(teacherNo=account)

                    if user.stuPassword == password:
                        request.session['is_login'] = True
                        request.session['user_id'] = account

                        No = account

                        return render(request, 'tutor.html', locals())
                    else:
                        message = "密码不正确！"
                else:
                    message = "用户类型错误"

            except Exception as e:
                print(e)
                message = "用户不存在！"

        return render(request, 'login.html', locals())


def student(request):
    return render(request, 'index_student.html')
