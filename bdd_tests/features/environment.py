# bdd_tests/environment.py

import asyncio
from playwright.async_api import async_playwright

def before_all(context):
    context.loop = asyncio.new_event_loop()
    asyncio.set_event_loop(context.loop)

def before_scenario(context, scenario):
    async def start_browser():
        context.playwright = await async_playwright().start()
        context.browser = await context.playwright.chromium.launch(headless=False)
        context.context = await context.browser.new_context()
        context.page = await context.context.new_page()
    
    context.loop.run_until_complete(start_browser())

def after_scenario(context, scenario):
    async def close_browser():
        if hasattr(context, "context"):
            await context.context.close()
        if hasattr(context, "browser"):
            await context.browser.close()
        if hasattr(context, "playwright"):
            await context.playwright.stop()

    context.loop.run_until_complete(close_browser())
