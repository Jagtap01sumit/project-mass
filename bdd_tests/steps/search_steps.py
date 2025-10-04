from behave import given, when, then
from playwright.sync_api import sync_playwright
from bdd_tests.pageObjects.LaunchBrowserPageObject import SearchPageLocators

@given("I open Google homepage")
def step_open_google(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)
    context.page = context.browser.new_page()
    context.page.goto("https://www.google.com")

@when('I search for "{keyword}"')
def step_search_keyword(context, keyword):
    context.page.fill(SearchPageLocators.SEARCH_BOX, keyword)
    context.page.press(SearchPageLocators.SEARCH_BOX, "Enter")
    context.page.wait_for_selector(SearchPageLocators.RESULTS)

@then("I should see results on the first page")
def step_validate_results(context):
    results = context.page.query_selector_all(SearchPageLocators.RESULTS)
    assert len(results) > 0, "❌ No results found!"
    print(f"✅ Found {len(results)} results on first page")

    context.browser.close()
    context.playwright.stop()
