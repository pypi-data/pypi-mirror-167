from microservice_template_core.tools.logger import get_logger
from microservice_template_core.settings import KafkaConfig
import traceback
from prometheus_client import Summary
from confluent_kafka import Producer
import json
import datetime

logger = get_logger()


class KafkaProduceMessages(object):
    KAFKA_PRODUCER_START = Summary('kafka_confluent_producer_start_latency_seconds', 'Time spent starting Kafka producer')
    KAFKA_PRODUCE_MESSAGES = Summary('kafka_confluent_produce_messages_latency_seconds', 'Time spent processing produce to Kafka')

    def __init__(self):
        self.producer = self.init_producer()

    @staticmethod
    @KAFKA_PRODUCER_START.time()
    def init_producer():
        try:
            producer_config = {
                'bootstrap.servers': KafkaConfig.KAFKA_SERVERS
                # 'message.send.max.retries': KafkaConfig.producer_message_send_max_retries,
                # 'retry.backoff.ms': KafkaConfig.producer_retry_backoff_ms,
                # 'queue.buffering.max.ms': KafkaConfig.producer_queue_buffering_max_ms,
                # 'queue.buffering.max.messages': KafkaConfig.producer_queue_buffering_max_messages,
                # 'request.timeout.ms': KafkaConfig.producer_request_timeout_ms
            }

            producer = Producer(**producer_config)

            return producer
        except Exception as err:
            logger.error(
                msg=f"Can`t connect to Kafka cluster - {KafkaConfig.KAFKA_SERVERS}\nError: {err}\nTrace: {traceback.format_exc()}"
            )
            return None

    @staticmethod
    def default_converter(o):
        if isinstance(o, (datetime.date, datetime.datetime)):
            return o.isoformat()

    @staticmethod
    def delivery_report(err, msg):
        """ Called once for each message produced to indicate delivery result.
            Triggered by poll() or flush(). """
        if err is not None:
            logger.error('Message delivery failed: {}'.format(err))
        # else:
            # logger.debug('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

    @KAFKA_PRODUCE_MESSAGES.time()
    def produce_message(self, topic, message):
        # logger.debug(
        #     msg=f"Start producing message to topic - {topic}\nBody: {message}"
        # )
        try:
            self.producer.produce(
                topic,
                json.dumps(message, default=self.default_converter).encode(),
                callback=self.delivery_report
            )

            self.producer.flush()
        except Exception as err:
            logger.error(
                msg=f"Can`t push message to - {topic}\nBody: {message}\nError: {err}\nTrace: {traceback.format_exc()}"
            )
