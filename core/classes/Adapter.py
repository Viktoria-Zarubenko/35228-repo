class Target:
    def default_reading_db(self) -> str:
        # domyslne zachowanie
        database_file = open("storage/db.txt", "r")
        return database_file.read()


class Adaptee:
    def reading_db_to_list(self, database_stream) -> list:
        data_for_ui = list(database_stream.split("\n"))
        return data_for_ui


class Adapter(Target, Adaptee):
    def default_reading_db(self) -> list:
        # nowe zachowanie
        database_file = open("storage/db.txt", "r")
        return self.reading_db_to_list(database_file.read())