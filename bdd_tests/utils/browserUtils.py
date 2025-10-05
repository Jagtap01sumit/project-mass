# bdd_tests/pageObjects/my_class_order_page.py

from bdd_tests.features.steps.BaseClass import BasePageObject
from playwright.async_api import Page
import os
from datetime import datetime

class Browser(BasePageObject):
    RESPONSIVE_VIEWS = {
    "mobile": {"width": 375, "height": 667},
    "tablet": {"width": 768, "height": 1024},
    "desktop": {"width": 1366, "height": 768}
}
    def __init__(self, page: Page, context_object):
        super().__init__(page)
        self.context_object = context_object

        # Element locators
        self.searchbar_xpath = "//div[text()='search']"

    async def enter_search(self, text):
        await self.page.fill(self.searchbar_xpath, text)

    async def click_search(self):
        await self.page.click(self.searchbar_xpath)
    @staticmethod
    async def take_screenshot(page: Page = None, name: str = "screenshot.png", folder: str = "bdd_tests/screenshots"):
        """Take a screenshot of the current page."""

        # Use page if provided, otherwise fallback to Browser._page
        page = page or Browser._page
        if page is None:
            raise Exception(" No Playwright page instance available for screenshot.")

        # Ensure the folder exists
        os.makedirs(folder, exist_ok=True)

        # Auto-generate name if not provided
        if not name or name.strip() == "":
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            name = f"screenshot_{timestamp}.png"

        # Ensure it ends with .png
        if not name.endswith(".png"):
            name += ".png"

        path = os.path.join(folder, name)

        # Take screenshot
        await page.screenshot(path=path)
        print(f" Screenshot saved: {path}")
        return path
    
    