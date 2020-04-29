from django.db import models


# Create your models here.


class Stu_info(models.Model):
    studentNo = models.CharField('学号', primary_key=True, max_length=8)
    stuPassword = models.CharField('密码', max_length=12)
    questionNo = models.ForeignKey('Question_info', on_delete=models.CASCADE)
    answer = models.CharField('密保答案', max_length=30)
    stuState = models.BooleanField('状态')

    class Meta:
        db_table = 'stu_info'


class Question_info(models.Model):
    questionNo = models.AutoField('密保问题编号', primary_key=True, max_length=11)
    question = models.CharField('密保问题', max_length=30)

    class Meta:
        db_table = 'question_info'


class Tec_info(models.Model):
    teacherNo = models.CharField('学号', primary_key=True, max_length=8)
    tecPassword = models.CharField('密码', max_length=12)
    questionNo = models.ForeignKey('Question_info', on_delete=models.CASCADE)
    answer = models.CharField('密保答案', max_length=30)
    tecState = models.BooleanField('状态')

    class Meta:
        db_table = 'tec_info'
