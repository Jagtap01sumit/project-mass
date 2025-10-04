from playwright.sync_api import sync_playwright
import os
from datetime import datetime

class Browser:
    _playwright = None
    _browser = None
    _context = None
    _page = None

    @staticmethod
    def start_browser(headless=False):
        """Start a new browser and return the page."""
        if Browser._playwright is None:
            Browser._playwright = sync_playwright().start()
            Browser._browser = Browser._playwright.chromium.launch(headless=headless)
            Browser._context = Browser._browser.new_context()
            Browser._page = Browser._context.new_page()
        return Browser._page

    @staticmethod
    def close_browser():
        """Close browser and stop Playwright."""
        if Browser._browser:
            Browser._browser.close()
        if Browser._playwright:
            Browser._playwright.stop()
        Browser._playwright = Browser._browser = Browser._context = Browser._page = None

    @staticmethod
    async def take_screenshot(name=None, folder="screenshots"):
        """Take a screenshot of the current page."""
        if Browser._page is None:
            raise Exception("Browser is not started. Call start_browser() first.")

       # crate folder is not exists
        if not os.path.exists(folder):
            os.makedirs(folder)

        # create file 
        if not name:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            name = f"screenshot_{timestamp}.png"

        path = os.path.join(folder, name)
        await Browser._page.screenshot({ path: name });
        print(f"📸 Screenshot saved: {path}")
        return path