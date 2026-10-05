from src.order_service import (
    EmailNotifier,
    OrderService,
    PushNotifier,
    SMSNotifier,
)


def test_email_notification():
    notifier = EmailNotifier()

    result = notifier.send("Alice", "Shipped")

    assert result == "EMAIL: Order for Alice is Shipped"


def test_sms_notification():
    notifier = SMSNotifier()

    result = notifier.send("Alice", "Shipped")

    assert result == "SMS: Order for Alice is Shipped"


def test_push_notification():
    notifier = PushNotifier()

    result = notifier.send("Alice", "Shipped")

    assert result == "PUSH: Order for Alice is Shipped"


def test_order_service_notifies_all():
    service = OrderService()

    service.add_notifier(EmailNotifier())
    service.add_notifier(SMSNotifier())
    service.add_notifier(PushNotifier())

    result = service.change_status("Alice", "Shipped")

    assert len(result) == 3
