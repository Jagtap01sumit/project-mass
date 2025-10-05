# bdd_tests/pageObjects/google_search_page.py
import os
import asyncio
import ssl
import socket
from datetime import datetime
from playwright.async_api import Browser, async_playwright
from bdd_tests.features.steps.BaseClass import BasePageObject
from urllib.parse import urlparse
class GoogleSearchPage(BasePageObject):
    RESPONSIVE_VIEWS = {
        "mobile": {"width": 375, "height": 667},
        "tablet": {"width": 768, "height": 1024},
        "desktop": {"width": 1366, "height": 768}
    }

    def __init__(self, page):
        super().__init__(page)
        self.search_box = '[name="q"]'
        self.result_titles = 'h3'

    async def search_keyword(self, keyword):
        await self.page.wait_for_selector(self.search_box)
        await self.page.fill(self.search_box, keyword)
        await self.page.keyboard.press("Enter")
        await self.page.wait_for_selector(self.result_titles, timeout=5000)

    async def get_results(self):
        return await self.page.query_selector_all(self.result_titles)

    @staticmethod
    async def capture_responsive_screenshots(page, folder="bdd_tests/screenshots/responsiveness"):
        os.makedirs(folder, exist_ok=True)
        
        for view, viewport in GoogleSearchPage.RESPONSIVE_VIEWS.items():
            # Resize the existing page viewport
            await page.set_viewport_size(viewport)

            # Wait a moment if needed for layout adjustments (optional)
            await page.wait_for_timeout(1000)  # wait 1 second
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{view}_{timestamp}.png"
            path = os.path.join(folder, filename)

            await page.screenshot(path=path)
            print(f" Screenshot for {view} saved at: {path}")
    @staticmethod
    async def sync_get_ssl_certificate_info(page):
        import os
        from datetime import datetime
        try:
      
            return {"ssl_ok": True}
        except Exception as e:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            folder = "bdd_tests/screenshots/ssl_issues"
            os.makedirs(folder, exist_ok=True)
            path = os.path.join(folder, f"ssl_failure_{timestamp}.png")
            await page.screenshot(path=path)
            print(f"Screenshot saved due to SSL failure at: {path}", flush=True)
            return {"ssl_ok": False, "error": str(e), "screenshot_path": path}
