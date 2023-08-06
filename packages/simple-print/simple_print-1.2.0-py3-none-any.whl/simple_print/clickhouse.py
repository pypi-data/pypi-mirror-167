import os 
from clickhouse_driver import Client as ClickHouseClient


def load_env():
    folder_path = os.path.dirname(os.path.realpath(__file__))
    with open(f"{folder_path}/clickhouse.env", 'r') as f:
       return dict(tuple(line.replace('\n', '').split('=')) for line in f.readlines() if not line.startswith('#'))


'''
README FIRST.

You can send messages to Clickhouse directly from RabbitMQ.

1) Read this article: https://clickhouse.com/docs/ru/engines/table-engines/integrations/rabbitmq/
2) Setup RabbitMQ credentials in clickhouse config file:
<rabbitmq>
    <username>user</username>
    <password>password</password>
    <vhost>vhost</vhost>
</rabbitmq>

3) Install Clickhouse driver: pip install clickhouse-driver
4) Run creation script: python -c "from simple_print import clickhouse; clickhouse.create_clickhouse_table()"
5) If you want to truncate table: python -c "from simple_print import clickhouse; clickhouse.truncate_clickhouse_table()"
'''


def create_clickhouse_table() -> None:
    # python -c "from simple_print import clickhouse; clickhouse.create_clickhouse_table()"
    ENV = load_env()
    assert ENV["SIMPLE_PRINT_CLICKHOUSE_HOST"], "Please specify SIMPLE_PRINT_CLICKHOUSE_HOST in your settings.py file"
    
    clickhouse_client = ClickHouseClient(
        host=ENV["SIMPLE_PRINT_CLICKHOUSE_HOST"], 
        port=ENV["SIMPLE_PRINT_CLICKHOUSE_PORT"],
        user=ENV["SIMPLE_PRINT_CLICKHOUSE_USER"], 
        password=ENV["SIMPLE_PRINT_CLICKHOUSE_PASSWORD"],
    )
    clickhouse_client.execute('DROP DATABASE IF EXISTS simple_print')
    clickhouse_client.execute('CREATE DATABASE simple_print')
    clickhouse_client.execute('DROP TABLE IF EXISTS simple_print.clickhouse_queue')
    clickhouse_client.execute('DROP TABLE IF EXISTS simple_print.records')
    
    clickhouse_client.execute(f'''
    CREATE TABLE simple_print.clickhouse_queue (
        `uuid` String,       
        `tag` String, 
        `args` Nullable(String),  
        `msg` Nullable(String),  
        `created` DateTime   
    ) 
    ENGINE = RabbitMQ             
    SETTINGS
        rabbitmq_host_port = '{ENV["SIMPLE_PRINT_RABBITMQ_HOST"]}:{ENV["SIMPLE_PRINT_RABBITMQ_PORT"]}',
                                rabbitmq_exchange_name = 'simple_print_exchange',
                                rabbitmq_routing_key_list = 'sprint, simple_print',
                                rabbitmq_format = 'JSONEachRow',
                                date_time_input_format = 'best_effort';
    ''')

    clickhouse_client.execute(f'''
    CREATE TABLE simple_print.records 
    (
        `uuid` String,       
        `tag` String, 
        `args` Nullable(String),  
        `msg` Nullable(String),  
        `created` DateTime  
    )     
    ENGINE = MergeTree()
    PARTITION BY toDate(created)
    ORDER BY (uuid) 
    TTL created + INTERVAL {ENV["SIMPLE_PRINT_CLICKHOUSE_TTL_DAY"]} DAY  
    SETTINGS min_bytes_for_wide_part = 0;  
    ''')

    clickhouse_client.execute(f'''
    CREATE MATERIALIZED VIEW simple_print.records_view TO simple_print.records
        AS SELECT * FROM simple_print.clickhouse_queue;                                        
    ''')
    print(f'success create; log rotation {ENV["SIMPLE_PRINT_CLICKHOUSE_TTL_DAY"]} day')


def truncate_clickhouse_table() -> None:
    # python -c "from simple_print import clickhouse; clickhouse.truncate_clickhouse_table()"
    ENV = load_env()
    assert ENV["SIMPLE_PRINT_CLICKHOUSE_HOST"], "Please specify SIMPLE_PRINT_CLICKHOUSE_HOST in your settings.py file"

    clickhouse_client = ClickHouseClient(
        host=ENV["SIMPLE_PRINT_CLICKHOUSE_HOST"], 
        port=ENV["SIMPLE_PRINT_CLICKHOUSE_PORT"],
        user=ENV["SIMPLE_PRINT_CLICKHOUSE_USER"], 
        password=ENV["SIMPLE_PRINT_CLICKHOUSE_PASSWORD"],
    )    
    clickhouse_client.execute('TRUNCATE TABLE IF EXISTS simple_print.records')
    print(f'success truncate')
