# Singleton - one single instance 
# If you want a new instance you will get the old one (already created) instance
class Singleton:
    __instance = None
    def __init__(self) -> None:
        if Singleton.__instance is None:
            Singleton.__instance = self
        else:
            raise Exception('This is singleton.Already have an instancce ,use that one by calling get_instance method')

    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

first= Singleton.get_instance()
Second= Singleton.get_instance()
third= Singleton.get_instance()
print(first)
print(Second)
print(third)

        
