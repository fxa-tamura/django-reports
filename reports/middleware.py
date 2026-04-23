import time
from django.conf import settings
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse


class AutoLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            current_time = int(time.time())
            last_activity = request.session.get('last_activity')

            # 一定時間以上操作がなければログアウト
            if last_activity:
                elapsed = current_time - last_activity
                if elapsed > settings.AUTO_LOGOUT_DELAY:
                    logout(request)
                    request.session.flush()
                    return redirect(reverse('login'))

            # 最終操作時刻を更新
            request.session['last_activity'] = current_time

        response = self.get_response(request)
        return response