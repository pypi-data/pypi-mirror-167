__version__ = '0.1.0'


import logging

from python_rabbitmq.connection import RMQConnection  # noqa
from python_rabbitmq.consumer import RMQConsumer  # noqa
from python_rabbitmq.producer import RMQProducer  # noqa
from python_rabbitmq.defs import (  # noqa
    QueueParams,
    ExchangeParams,
    QueueBindParams,
    ConsumeParams,
    PublishParams,
    ConsumeOK,
    ConfirmModeOK,
    DeliveryError,
    DEFAULT_EXCHANGE,
    MandatoryError
)


logging.getLogger(__name__).addHandler(logging.NullHandler())