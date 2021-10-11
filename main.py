def logger(text: str):
    print(f'lolz ale fajny tekst: {text}')


class IFactory:
    pass


class HelloWorldFactory(IFactory):
    def implement(self):
        print("Hello Hello")
