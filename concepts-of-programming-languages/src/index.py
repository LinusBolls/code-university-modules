#! /usr/bin/python3

"""
dings
"""

from abc import ABC, abstractmethod

class GreetingModel(ABC):
    @property
    @abstractmethod
    def message(self):
        pass

class GreetingView(ABC):
    @abstractmethod
    def display(self):
        pass

class MoinMeisterModel(GreetingModel):
    message = "moin meister"

class ServusModel(GreetingModel):
    message = "servus maggus"

try:
    class InvalidGreetingModel(GreetingModel):
        not_message = "this will throw"

except Exception:
    print("exception occured")



class PrintView(GreetingView):
    def display(self, str):
        print(str)

class FileView(GreetingView):
    def display(self, str):
        with open('out.txt', 'w') as f:
            f.write(str)



class GreetingController:
    def __init__(self, greeting_model, greeting_view):
        self.model = greeting_model
        self.view = greeting_view

    def greet(self):
        self.view.display(self.model.message)


def main():
    GreetingController(MoinMeisterModel(), PrintView()).greet()

    GreetingController(ServusModel(), FileView()).greet()

if __name__ == "__main__":
    main()
