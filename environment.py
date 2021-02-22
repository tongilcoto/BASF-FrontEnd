from screenshotFileName import get_screenshot_new_file_name
from behave.model_core import Status


def after_step(context, step):
    if step.status == Status.failed:
        context.failed_step_name = step.keyword + ' ' + step.name


def after_scenario(context, scenario):
    if context.failed:
        context.current_page.save_screenshot(get_screenshot_new_file_name(scenario.name, context.failed_step_name))
    context.current_page.close()

