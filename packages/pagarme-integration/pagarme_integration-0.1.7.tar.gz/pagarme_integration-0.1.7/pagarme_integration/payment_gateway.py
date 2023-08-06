from jsonschema.exceptions import ValidationError, SchemaError
from jsonschema import validate

from pagarme_integration.classes.customers import Customer
from pagarme_integration.classes.config import Config
from pagarme_integration.classes.orders import Order
from pagarme_integration.classes.cards import Card


class PaymentGatewayClass:
    def __init__(self, key) -> None:
        Config.set_auth(key=key)

    def get_customers(self):
        return Customer.get_customers()

    def get_customer(self, pk):
        return Customer.get_customer(pk=pk)

    def insert_customer(self, payload):
        try:
            validate(instance=payload, schema=Customer.validate_insert())
            return Customer.insert_customer(payload=Customer.mount_obj(content=payload))
        except ValidationError as ve:
            raise ve
        except SchemaError as se:
            raise se

    def get_cards(self, customer_id):
        return Card.get_cards(customer_id=customer_id)

    def get_card(self, customer_id, pk):
        return Card.get_card(customer_id=customer_id, pk=pk)

    def insert_card(self, customer_id, payload):
        try:
            validate(instance=payload, schema=Card.validate_insert())
            return Card.insert_card(
                customer_id=customer_id, payload=Card.mount_obj(content=payload)
            )
        except ValidationError as ve:
            raise ve

    def get_orders(self, customer_id=None):
        return Order.get_orders(customer_id=customer_id)

    def get_order(self, pk):
        return Order.get_order(pk=pk)

    def insert_order(self, payload):
        try:
            validate(instance=payload, schema=Order.validate_insert())
            return Order.insert_order(payload=Order.mount_obj(content=payload))
        except ValidationError as ve:
            raise ve
