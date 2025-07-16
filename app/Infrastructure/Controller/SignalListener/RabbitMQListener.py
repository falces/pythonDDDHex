from app import signals
from flask import Blueprint
import pika
import datetime
from flask import current_app as app
from Infrastructure.Exceptions.RabbitMQException import RabbitMQException

rabbitMQSignalListener = Blueprint('rabbitMQSignalListener', __name__)

class RabbitConnection():

    def connect(self):
        try:
            rabbitmq_host = app.config['RABBITMQ_HOST']
            rabbitmq_port = app.config['RABBITMQ_PORT']
            rabbitmq_vhost = app.config['RABBITMQ_VHOST']
            rabbitmq_user = app.config['RABBITMQ_USER']
            rabbitmq_password = app.config['RABBITMQ_PASS']

            credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_password)

            parameters = pika.ConnectionParameters(
                    host=rabbitmq_host,
                    port=rabbitmq_port,
                    virtual_host=rabbitmq_vhost,
                    credentials=credentials
                )

            self.connection = pika.BlockingConnection(
                parameters
            )

            channel = self.connection.channel()
            channel.queue_declare(queue='3plapi')

            return channel

        except (Exception, pika.exceptions.AMQPConnectionError) as e:
            raise RabbitMQException(e)
        finally:
            if 'connection' in locals() and self.connection.is_open:
                self.connection.close()


    def close(self):
        self.connection.close()

    def createMessage(
        self,
        sender: str,
        message: dict,
    ) -> str:
        content = {
            'id': sender,
            'datetime': datetime.datetime.now().isoformat(),
            'data': message,
        }

        return str(content)


class RabbitMQSignalListener():

    @signals['new_country_created'].connect
    def newRabbitMQMessage(
        self,
        sender: str,
        message: dict,
    ):
        rabbit = RabbitConnection()
        channel = rabbit.connect()

        channel.basic_publish(
            exchange = '',
            routing_key = '3plapi',
            body = rabbit.createMessage(
                sender,
                message,
            ),
        )

        rabbit.close()
