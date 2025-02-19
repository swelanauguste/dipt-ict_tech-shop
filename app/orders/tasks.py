from django.core.mail import send_mail

from .models import Order


def order_created(order_id):
    """
    Task to send an e-mail notification when an order is
    successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = f"Order nr. {order.oid}"
    message = (
        f"Dear {order.name},\n\n"
        f"You have successfully placed an order.\n\n"
        f"Your order ID is {order.oid}. \n\n"
        f"The total cost of your order is XCD${order.get_total_cost()}"
    )
    mail_sent = send_mail(subject, message, "kingship.lc@gmail.com", [order.email])
    return mail_sent
