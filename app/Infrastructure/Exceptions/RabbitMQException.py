class RabbitMQException(Exception):
    def __init__(self, message="RabbitMQ error"):
        self.message = message
        super().__init__(self.message)