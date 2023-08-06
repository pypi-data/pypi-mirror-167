from pagarme_integration.schemas.cards import CardSchema


class PaymentSchema:
    __get = {
        "type": "object",
        "properties": {
            "payment_method": {"type": "string"},
            "credit_card": CardSchema.validate_credit_card(),
        },
        "required": ["payment_method", "credit_card"],
    }

    @classmethod
    def validate_get(cls):
        return cls.__get
