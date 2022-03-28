class SingletonMeta(type):

    """
    Użycie metaclassy do implementacji Singletona.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def some_planer_business_logic(self, any_plan):

        """
        Logika logera dla planów użytkownika
        """
        
        return f"Planer Singleton result {any_plan}"