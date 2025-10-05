
from playwright.async_api import Page

class BasePageObject:
    def __init__(self, page: Page):
        self._page = page  

    @property
    def page(self) -> Page:
        return self._page 
