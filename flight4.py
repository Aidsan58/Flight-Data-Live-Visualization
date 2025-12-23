from pykafka import KafkaClient

# set up a Kafka client in Python by specifying the location of our Kafka broker
client = KafkaClient(hosts="localhost:9092")

# Connect newly spun consumer to flightdata topic
# For each message in the topic, we print out the message payload
for i in client.topics['flightdata'].get_simple_consumer():
    print('data:{0}\n\n'.format(i.value.decode()))