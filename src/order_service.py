class EmailNotifier:
    def send(self, customer, status):
        return f"EMAIL: Order for {customer} is {status}"


class SMSNotifier:
    def send(self, customer, status):
        return f"SMS: Order for {customer} is {status}"


class PushNotifier:
    def send(self, customer, status):
        return f"PUSH: Order for {customer} is {status}"


class OrderService:
    def __init__(self):
        self.notifiers = []

    def add_notifier(self, notifier):
        self.notifiers.append(notifier)

    def change_status(self, customer, status):
        messages = []

        for notifier in self.notifiers:
            messages.append(
                notifier.send(customer, status)
            )

        return messages
