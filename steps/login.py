from behave import given, when, then, use_step_matcher
from sut.model.login import QK_Login
from sut.model.termsofuse import QK_TermsOfUse
from sut.model.main import QK_Main

@given('I open QKnows log in page')
def step_open(context):
    context.login = QK_Login()
    context.current_page = context.login


@when('I set my user credentials')
def step_credentials(context):
    context.login.set_user_credentials()


@when('I select Log In option')
def step_login(context):
    login_next_page = context.login.login()
    context.terms_of_use = QK_TermsOfUse(login_next_page)
    if context.terms_of_use.is_terms_of_use_present():
        context.terms_of_use.accept_terms_of_use()
        context.main = QK_Main(context.terms_of_use.proceed())
    else:
        context.main = QK_Main(login_next_page)
    context.current_page = context.main


@then('I access QKnows main page')
def step_main(context):
    assert context.main.get_title_value() == 'QKnows'


use_step_matcher("re")
@then('"(?P<field>search field|search magnifier|Upcoming Events section|News section|access to Support chat)" is visible')
def step_layout(context, field):
    context.main.verify_field_visibility(field)
