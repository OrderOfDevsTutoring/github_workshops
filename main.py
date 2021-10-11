from typing import Protocol


def logger(text: str):
    print(f'lolz ale fajny tekst: {text}')


class Logger:
    def info(self, text: str):
        print(f'Logger: {text}')


class Factory(Protocol):
    pass


logger = Logger()


class HelloWorld(Factory):
    def execute(self):
        logger.info('HelloWorld')
        print('Hello world')


HelloWorld().execute()
