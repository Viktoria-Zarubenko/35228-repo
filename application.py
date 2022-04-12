import eel

from core.classes.Adapter import Adaptee
from core.classes.Facade import Facade
from core.classes.Iterator import sort_plans
from core.classes.TemplateMethod import run_template_functions


@eel.expose
def save_data_from_ui(plan_text: str, deadline: str):
    savingProcess = Facade()
    savingProcess.process(plan_text, deadline)

    adaptee = Adaptee()
    database_file = open("storage/db.txt", "r")
    data_for_ui = adaptee.reading_db_to_list(database_file.read())
    print(data_for_ui)


@eel.expose
def send_plans_to_ui(input_plans=[]):
    if input_plans:
        plans = input_plans
    else:
        plans = list(open('storage/db.txt'))

    plans_html = ''

    for plan in plans:
        plan_number = plans.index(plan) + 1
        plan_desc = plan.rsplit(':', 1)[0]
        plan_deadline = plan.rsplit(':', 1)[1]
        plans_html += "<tr><th scope='row'>{}</th><td>{}</td><td>{}</td><td><button class='btn btn-outline-danger' id='{}' onclick=get_plan_info('{}')><i class='fas fa-question-circle'></i></button></td></tr>".format(
            plan_number, plan_desc, plan_deadline, plan, plan)

    if len(plans) == 0:
        eel.show_plans(
            "<tr><td colspan='3'>Nie masz jeszcze żadnych planów. Dodaj je!</td></tr>")
    else:
        eel.show_plans(plans_html)


@eel.expose
def sort_plans_via_iterator():
    not_sorted_plans = list(open('storage/db.txt'))
    sorted_plans = sort_plans(not_sorted_plans)
    send_plans_to_ui(sorted_plans)


@eel.expose
def template_example():
    run_template_functions()


if __name__ == "__main__":
    eel.init('web')
    eel.start("index.html", mode="electron")
