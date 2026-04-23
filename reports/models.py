from django.db import models
from django.contrib.auth.models import User


class Report(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    department = models.CharField('所属', max_length=100, blank=True)
    employee_name = models.CharField('氏名', max_length=100, blank=True)
    work_date = models.DateField('作業日')
    goal = models.CharField('目標', max_length=255, blank=True)

    task1 = models.CharField('タスク1', max_length=255, blank=True)
    task2 = models.CharField('タスク2', max_length=255, blank=True)
    task3 = models.CharField('タスク3', max_length=255, blank=True)

    work_time1 = models.CharField('時間1', max_length=50, blank=True)
    work_detail1 = models.CharField('業務詳細1', max_length=255, blank=True)

    work_time2 = models.CharField('時間2', max_length=50, blank=True)
    work_detail2 = models.CharField('業務詳細2', max_length=255, blank=True)

    work_time3 = models.CharField('時間3', max_length=50, blank=True)
    work_detail3 = models.CharField('業務詳細3', max_length=255, blank=True)

    work_time4 = models.CharField('時間4', max_length=50, blank=True)
    work_detail4 = models.CharField('業務詳細4', max_length=255, blank=True)

    summary = models.TextField('総括', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.work_date} / {self.employee_name or "日報"}'