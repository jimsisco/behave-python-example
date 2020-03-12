from behave import *


@given('i have internet connectivity')
def step(context):
    pass


@when('we visit kindercare')
def step(context):
    context.browser.get('http://kindercare.com')


@then('it should have a title "KinderCare | Child Daycare Centers & Early Education Programs"')
def step(context):
    assert context.browser.title == "KinderCare | Child Daycare Centers & Early Education Programs"


@then('I click Find Your Center')
def step(context):
    # click submit button
    submit_button = context.browser.find_elements_by_xpath('//*[@id="homePage"]/div/div/div[2]/a')[0].click()


@then('it should have taken me to "Center Search Results | KinderCare"')
def step(context):
    assert context.browser.title == "Center Search Results | KinderCare"


@then('i enter my zip code')
def step(context):
    text_area = context.browser.find_element_by_xpath('//*[@id="center-search-location"]')
    text_area.clear()
    text_area.send_keys("97236")


@then('and click Search Again')
def step(context):
    context.browser.find_element_by_xpath('//main[@id=\'main\']/div[2]/aside/div[2]/form/fieldset[4]/button').click()


@then('i can see the center and click Tuition and Openings')
def step(context):
    context.browser.find_element_by_xpath('//li[@id=\'300902\']/div/div[2]/a').click()


@then('i can see "Powell KinderCare"')
def step(context):
    # result = driver.find_element_by_xpath('//li[@id=\'300902\']/div/a/h2')
    assert context.browser.title == "Center Search Results | KinderCare"

