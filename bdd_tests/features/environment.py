
from bdd_tests.utils.browserUtils import Browser

def before_scenario(context, scenario):
    """Automatically runs before each scenario"""
    context.page = Browser.start_browser(headless=False)

# def after_scenario(context, scenario):
#     """Automatically runs after each scenario"""
    # Browser.close_browser()
