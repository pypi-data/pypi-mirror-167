import os
import pika
import json
from typing import Union
from terminaltables import AsciiTable


SIMPLE_PRINT_RABBITMQ_URI = os.getenv("SIMPLE_PRINT_RABBITMQ_URI")


def catch(tag:Union[str, None]="sprint", queue:str="simple_print_queue", count:int=10, as_list:bool=False, **kwargs):
    """ 
    catch - simple functions to catch messages from RabbitMQ queues

    signature:
    tag:Union[str, None] ~ message tag
    queue:str="simple_print_queue" ~ rabbitmq queue name
    count:int=10 ~ count messages
    as_list:bool=False ~ return as list
    """  

    assert SIMPLE_PRINT_RABBITMQ_URI, "Please specify SIMPLE_PRINT_RABBITMQ_URI in ENVIRONMENT"
    if tag: assert tag.isascii() and len(tag) < 256, "Invalid tag name"
    assert queue.isascii() and len(queue) < 256, "Invalid RabbitMQ queue name"

    messages = []
    connection = pika.BlockingConnection(pika.URLParameters(SIMPLE_PRINT_RABBITMQ_URI))
    channel = connection.channel()
    for _ in range(count):
        method_frame, header_frame, body = channel.basic_get(queue)
        if method_frame:
            message = json.loads(body.decode())
            if message["tag"] == tag or not tag:
                messages.append(message)
                channel.basic_ack(method_frame.delivery_tag)

    if as_list:
        return messages
    else:
        [print(body, "\n", "x" * 50) for body in messages]

