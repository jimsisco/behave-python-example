from selenium import webdriver


def before_all(context):
    context.browser = webdriver.Chrome()
    context.browser.set_page_load_timeout(10)
    context.browser.implicitly_wait(5)
    return context


