from web_source.web_factory import get_web
#from selenium import webdriver


def before_all(context):
    web = get_web(context.config.userdata['browser'])
    context.web = web


