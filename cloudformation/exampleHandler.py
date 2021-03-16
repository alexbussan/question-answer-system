class ExampleHandler:
    def handle(self, event, context=None):
        print("hello, looks like this is working")

        return "SUCCESS"


def handler(event, context):
    return ExampleHandler().handle(event, context)