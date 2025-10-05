from behave import given, when, then
from bdd_tests.pageObjects.LaunchBrowserPageObject import GoogleSearchPage
from bdd_tests.utils.browserUtils import Browser
from urllib.parse import urlparse
import traceback
from behave.runner import Context

import os
from dotenv import load_dotenv

load_dotenv() 


@given('I launch the browser and search for URL')
async def step_impl(context):
    url = os.getenv("TARGET_URL")
    if not url:
        raise ValueError("TARGET_URL is not set in environment variables!")

    try:
        print(f"[INFO] Opening URL: {url}")
        await context.page.goto(url)
        await context.page.wait_for_load_state("load")
    except Exception as e:
        print(f"[Step Failed] launch browser and open URL '{url}': {e}")
        traceback.print_exc()

@when('I search for "{keyword}"')
async def step_search_keyword(context, keyword):
    try:
        search_page = GoogleSearchPage(context.page)
        await search_page.search_keyword(keyword)
        await Browser.take_screenshot(context.page, name="search_results")
    except Exception as e:
        print(f"[Step Failed] search for '{keyword}': {e}", flush=True)
        traceback.print_exc()

@then("I should see results on the page")
async def step_validate_results(context):
    try:
        search_page = GoogleSearchPage(context.page)
        results = await search_page.get_results()
        await Browser.take_screenshot(context.page, name="results_page")
        if not results or len(results) == 0:
            print("[Step Failed] No search results found!", flush=True)
        else:
            print(f"Found {len(results)} results.", flush=True)
    except Exception as e:
        print(f"[Step Failed] validate search results: {e}")
        traceback.print_exc()

@then("I save the responsiveness screenshots")
async def save_screenshots_of_responsiveness(context):
    try:
        await GoogleSearchPage.capture_responsive_screenshots(context.page)
    except Exception as e:
        print(f"[Step Failed] save responsiveness screenshots: {e}")
        traceback.print_exc()

@then('I verify SSL certificate is available and valid')
async def verify_ssl_certificate(context):
    try:
        result = await GoogleSearchPage.sync_get_ssl_certificate_info(context.page)
        assert result["ssl_ok"], f"SSL check failed: {result.get('error')}"
    except AssertionError as e:
        print(f"[Step Failed] verify SSL certificate: {e}", flush=True)
        raise  # re-raise so behave knows step failed and prints traceback
    except Exception as e:
        print(f"[Step Failed] Exception in SSL check: {e}", flush=True)
        raise
