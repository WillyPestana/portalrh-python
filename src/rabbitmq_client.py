import pika


def send_message_to_queue(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    channel.queue_declare(queue="fila_de_tarefas")
    channel.basic_publish(exchange="", routing_key="fila_de_tarefas", body=message)
    connection.close()


# Aqui falta o Consumer futuramente adicionado
