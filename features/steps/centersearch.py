import time
from behave import given, when, then


@given('I have internet connectivity')
def step(context):
    pass


@when('we visit kindercare')
def step(context):
    context.web.get('http://kindercare.com')


@then('it should have a title "KinderCare | Child Daycare Centers & Early Education Programs"')
def step(context):
    assert context.web.title == "KinderCare | Child Daycare Centers & Early Education Programs"
    context.web.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/button").click()


@then('I click Find Your Center')
def step(context):
    context.web.find_elements_by_xpath('//*[@id="homePage"]/div/div/div[2]/a')[0].click()


@then('it should have taken me to "Center Search Results | KinderCare"')
def step(context):
    assert context.web.title == "Center Search Results | KinderCare"


@then('I enter my zip code')
def step(context):
    text_area = context.web.find_element_by_xpath('//*[@id="center-search-location"]')
    text_area.clear()
    text_area.send_keys("97236")


@then('and click Search Again')
def step(context):
    context.web.find_element_by_xpath('//main[@id=\'main\']/div[2]/aside/div[2]/form/fieldset[4]/button').click()


@then('I can see the center and click Tuition and Openings')
def step(context):
    time.sleep(3)
    context.web.find_element_by_xpath('//li[@id=\'300902\']/div/div[2]/a').click()


@then('I can see "Center Search Results | KinderCare"')
def step(context):
    result = context.web.title
    assert result == "Center Search Results | KinderCare"


@then('I enter First Name')
def step(context):
    context.web.find_by_xpath('//*[@id="iframe-tuition-modal"]')
    fn_text = context.web.find_element_by_xpath('//input[@id=\'FirstName\']')
    fn_text.clear()
    fn_text.send_keys('First Name')




