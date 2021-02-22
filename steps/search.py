from behave import given, when, then
import random
import steps.login


@given('I proceed to QKnows main page')
def step_impl(context):
    steps.login.step_open(context)
    steps.login.step_credentials(context)
    steps.login.step_login(context)


@when('I search for a random meaningful word')
def step_impl(context):
    words = ['water', 'propylene', 'ethanol', 'carbon', 'silicon']
    context.word = random.choice(words)
    context.main.search_for_word(context.word)


@then('the first 3 results get the searched word')
def step_impl(context):
    context.main.verify_searched_word_in_abstracts(context.word)

