from observer import Observer


class Fan(Observer):

    def notify(self, *args, **kwargs):

        if args[1] > 28:
            print("Wiatrak wyłączony")
        elif args[1] < 23:
            print("Wiatrak włączony")
        else:
            print("Wiatrak bez zmian")
