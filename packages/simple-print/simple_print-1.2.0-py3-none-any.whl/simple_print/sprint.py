import os
import pika
import json
import inspect
import traceback
from secrets import token_hex
from datetime import datetime
from pydantic import Field, BaseModel
from typing import Optional, Any, Union
from termcolor import cprint
from executing import Source


DEBUG = os.getenv("DEBUG","").lower() in ("1", "true", "yes", "y")
SIMPLE_PRINT_PATH_TO_FILE = os.getenv("SPRINT_PATH_TO_FILE","").lower() in ("1", "true", "yes", "y")
SIMPLE_PRINT_RABBITMQ_URI = os.getenv("SIMPLE_PRINT_RABBITMQ_URI")


class BrokerMessage(BaseModel):
    broker: Optional[str] = 'rabbitmq'
    queue: Optional[str] = 'simple_print_queue'
    tag: Optional[str] = 'sprint'
    msg: Optional[dict] = {}
    uuid: Optional[str] = token_hex(16) 
    created: datetime = Field(default_factory=datetime.utcnow)


def _colored_print(arg:Any, arg_name:str, c:str, b:str, a:str, p:str, lineno:int, filename:str) -> None:  
    if b:
        if p:
            cprint(f'>>> {arg_name} | type {type(arg)} | line {lineno} | file {filename}', c, b, attrs=[a])
        else:
            cprint(f'>>> {arg_name} | type {type(arg)} | line {lineno}', c, b, attrs=[a])
    else:
        if p:
            cprint(f'>>> {arg_name} | type {type(arg)} | line {lineno} | file {filename}', c, attrs=[a])
        else:
            cprint(f'>>> {arg_name} | type {type(arg)} | line {lineno}', c, attrs=[a])


def sprint(*args, c:str ="white", b:str ="", a:str="bold", p:bool=SIMPLE_PRINT_PATH_TO_FILE, s:bool=False, broker:dict={}, **kwargs) -> Union[None, str]:
    ''' 
    Simple print https://github.com/Sobolev5/simple-print
    
    --- as console debugger ---
    # с:str ~ colors: ["grey", "red", "green", "yellow", "blue", "magenta", "cyan", "white"]
    # b:str ~ backgrounds: ["on_grey", "on_red", "on_green", "on_yellow", "on_blue", "on_magenta", "on_cyan"]
    # a:str ~ attributes: bold, dark, underline, blink, reverse, concealed 
    # p:bool ~ path: show path to file    
    # s:bool ~ string: return as string
    
    --- proxy through broker ---
    # broker:dict ~ proxy to broker: now only rabbitmq   
    requires ENV SIMPLE_PRINT_RABBITMQ_URI
    send json message to vhost.amq.direct.simple_print_queue
    
    message dict schema:
    {
     "queue": "simple_print_queue", # by default
     "tag": "tag", # `tag` by default
     "msg": "{'hello':'world'}" # any dict    
    }
    '''

    if DEBUG or broker:
        stack = traceback.extract_stack()
        filename, lineno, function_name, code = stack[-2]
        call_frame = inspect.currentframe().f_back
        call_node = Source.executing(call_frame).node
        source = Source.for_frame(call_frame)

        if s or broker:
            arg_names = []

        for i, arg in enumerate(args):
            try:
                arg_name = source.asttokens().get_text(call_node.args[i])
                arg_name = f"{arg}" if arg_name == arg else f"{arg_name} = {arg}"
            except:
                arg_name = f"{arg}"

            if s or broker:
                arg_name = f'{arg_name} | {type(arg)} | lineno {lineno} | file {filename}' if p else f'{arg_name} | {type(arg)} | lineno {lineno}'
                arg_names.append(arg_name)
            else:
                _colored_print(arg, arg_name, c, b, a, p, lineno, filename)
        
        if s:
            return ';'.join(arg_names)

        if broker:
            broker_msg = BrokerMessage(**broker)

            assert SIMPLE_PRINT_RABBITMQ_URI, "Please specify SIMPLE_PRINT_RABBITMQ_URI in ENVIRONMENT"
            assert broker_msg.tag.isascii() and len(broker_msg.tag) < 256, "Invalid tag name"
            assert broker_msg.queue.isascii() and len(broker_msg.queue) < 256, "Invalid RabbitMQ queue name"        

            connection = pika.BlockingConnection(pika.URLParameters(SIMPLE_PRINT_RABBITMQ_URI))
            channel = connection.channel()

            if broker_msg.queue == "clickhouse":
                body = {
                    "uuid": broker_msg.uuid,
                    "tag": broker_msg.tag,
                    "args": ';'.join(arg_names), 
                    "msg": broker_msg.msg,
                    "created": broker_msg.created.strftime("%Y-%m-%d %H:%M:%S") 
                }
                channel.basic_publish(exchange="simple_print_exchange", routing_key=f"sprint", properties=pika.BasicProperties(expiration=str(60000*60)), body=json.dumps(body))                
                connection.close()
            else:
                channel.queue_declare(queue=f"{broker_msg.queue}", durable=True)  
                body = {
                    "uuid": broker_msg.uuid,
                    "tag": broker_msg.tag,
                    "args": ';'.join(arg_names), 
                    "msg": broker_msg.msg,
                    "created": broker_msg.created.strftime("%Y-%m-%d %H:%M:%S") 
                }
                channel.basic_publish(exchange="", routing_key=f"{broker_msg.queue}", properties=pika.BasicProperties(expiration=str(60000*120)), body=json.dumps(body))                
                connection.close()