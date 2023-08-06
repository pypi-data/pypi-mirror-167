import os
from simple_print import sprint


def test_broker(): 
    SIMPLE_PRINT_RABBITMQ_URI = os.getenv("SIMPLE_PRINT_RABBITMQ_URI")
    assert SIMPLE_PRINT_RABBITMQ_URI, "SIMPLE_PRINT_RABBITMQ_URI is required"
    msg = {
        "hello": "world"
    }
    sprint("see you in rabbitmq queue", p=True, broker={"tag": "tag", "msg": msg})
