# ========================================
# 開発用アクセスURL
# ========================================

# ログイン  
# http://127.0.0.1:8000/reports/login/

# 一般ユーザー登録画面
# http://127.0.0.1:8000/reports/signup/

# 日報一覧（ログイン後トップ想定）
# http://127.0.0.1:8000/reports/

# 日報登録
# http://127.0.0.1:8000/reports/create/

# 管理画面
# http://127.0.0.1:8000/reports/admin-list/

"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
