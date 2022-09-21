from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
import asyncio
from util import get_entire_html, is_bot

class ssr (MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/':
            if is_bot(request):
                try:
                    protocol = 'https://' if request.is_secure() else 'http://'
                    url = protocol + request.get_host() + '/mirror' + request.path
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                    html = loop.run_until_complete(get_entire_html(url, '.target', 20))
                    return HttpResponse(html)
                except BaseException as err:
                    print(f"Unexpected {err}, {type(err)}")
