import eel

class SendingToast:
    def send_toast(self, plan_text: str, deadline: str):
        print(f'Added new plan: {plan_text}, {deadline}')


class Cleanup:
    def clear_inputs(self):
        eel.clearInputs()


class SavingData:
    def save_data(self, plan_text: str, deadline: str):
        txt_db_object = open('storage/db.txt', 'a')
        txt_db_object.write(f'{plan_text}:{deadline}\n')
        txt_db_object.close()

class Facade:
    def __init__(self):
        self.clearing_inputs = Cleanup()
        self.sending_toast = SendingToast()
        self.saving_data = SavingData()


    def process(self, plan_text: str, deadline: str):
        self.saving_data.save_data(plan_text, deadline)
        self.clearing_inputs.clear_inputs()
        self.sending_toast.send_toast(plan_text, deadline)