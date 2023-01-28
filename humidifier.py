from observer import Observer


class Humidifier(Observer):

    def notify(self, *args, **kwargs):
        if args[2] > 60:
            print("Nawilżacz wyłączony")
        elif args[2] < 30:
            print("Nawilżacz włączony")
        else :
            print("Nawilżacz bez zmian")

