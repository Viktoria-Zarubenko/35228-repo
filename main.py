from application.classes.SingletonLogger import Singleton
from application.classes import FactoryMethod


if __name__ == "__main__":

    # tworzymy dwie instancje singletona
    s1 = Singleton()
    s2 = Singleton()

    # tu wowolujemy funcje która będzie robiła jakąś logikę, czyli zapisywanie do bazy
    print(s1.some_planer_business_logic('plan 1'))
    print(s2.some_planer_business_logic('plan 2'))

    # w tym if'ie porównójemy czy faktycznie dwie instancje singletona to jest ta sama instacja
    if id(s1) == id(s2):
        print("\nPoprawnie wszystko zrobiliśmy, dwie instancje są takie same\n\n")
    else:
        print("\nCoś jest żle, instancje nie są równe")


    # użycie Factory na przykładzie dwóch testowych kreatorów
    print("Konkretny kreator - ConcreteCreator1.")
    FactoryMethod.client_code(FactoryMethod.ConcreteCreator1())

    print("\nKonkretny kreator - ConcreteCreator2.")
    FactoryMethod.client_code(FactoryMethod.ConcreteCreator2())