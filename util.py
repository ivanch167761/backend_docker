

#import requests

import socket
from django_user_agents.utils import get_user_agent

from ipware import get_client_ip

import asyncio
from pyppeteer import launch

async def get_entire_html(url, targetForWaiting, scrollTime):
    browser = await launch(
        handleSIGINT=False,
        handleSIGTERM=False,
        handleSIGHUP=False
    )
    page = await browser.newPage()
    await page.goto(url)

    await page.waitForSelector(targetForWaiting)
    for i in range(scrollTime):
        await page.evaluate("""{window.scrollBy(0, document.body.scrollHeight);}""")

    html = await page.content()

    await browser.close()
    return html

def is_bot(request):
    user_agent = get_user_agent(request)
    if not user_agent.is_bot:
        return False
    return True
