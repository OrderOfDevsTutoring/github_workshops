def logger(text: str):
    print(f'Logger: {text}')


class IFactory:
    pass


class HelloWorldFactory(IFactory):
    def execute(self):
        print("Hello world")
