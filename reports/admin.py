from django.contrib import admin
from .models import Report


# Reportモデルをadmin画面に表示する
# 管理画面からデータの追加・編集・削除ができるようになる
admin.site.register(Report)
