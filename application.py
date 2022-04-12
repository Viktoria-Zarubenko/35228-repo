import eel
from core.classes.Facade import Facade
from core.classes.Adapter import Adaptee

@eel.expose
def save_data_from_ui(plan_text: str, deadline: str):
    savingProcess = Facade()
    savingProcess.process(plan_text, deadline)

    adaptee = Adaptee()
    database_file = open("storage/db.txt", "r")
    data_for_ui = adaptee.reading_db_to_list(database_file.read())
    print(data_for_ui)



if __name__ == "__main__":
    eel.init('web')
    eel.start("index.html", mode="electron")
