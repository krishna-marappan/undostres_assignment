from behave import *
from Data import *
from feature_support.WebDriverSetup import *
from feature_support.undostres_support import *


@given("user,he or she is to launch an undostres website")
def website_launch(context):
    context.driver = WebDriverSetup.website_launch(Url.undostresurl)


@when("user fills in the Recarga Celular details, click on the siguiente")
def recarga_celular_details(context):
    undostres_support.recarga_celular_details(context.driver, number=Data.number, operator=Data.operator,
                                              amount=Data.amount)


@then("the user is able to reach the next screen (Payment screen)")
def payment_screen_verification(context):
    status = undostres_support.payment_screen_verify(context.driver)
    if status:
        print("user was able to reach the next screen(Payment screen)")
    else:
        print("user was not able to reach the next screen(Payment screen)")


@when("the user is able to enter payment information")
def payment_information(context):
    undostres_support.payment_details(context.driver, Cardnumber=Data.card_no, month=Data.exp_month,
                                      year=Data.exp_year, ccv=Data.ccv, email=Data.payment_email)


@when("the user is able to fill Access with mail fields")
def access_with_mail(context):
    undostres_support.access_with_email(context.driver, email=Data.email, Password=Data.password)


@then("the user gets a success message and the recharge is successful")
def success_message_verify(context):
    status = undostres_support.success_message_verify(context.driver)
    if status:
        print("user gets a success message and the recharge is successful")
    else:
        print("user does not get a success message.")


@then("users close all open browsers")
def browser_close(context):
    context.driver.quit()

