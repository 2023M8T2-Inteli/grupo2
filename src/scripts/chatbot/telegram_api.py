import telebot
from rclpy.node import Node
from std_msgs.msg import String
import rclpy


CHAVE_API = '6789925207:AAGWEl8dbtY3-C-EO3-g9gJQURvYQozIuaI'

bot = telebot.TeleBot(CHAVE_API)

class TelegramNode(Node):
    def __init__(self,chat_id):
        super().__init__('telegram_node')
        self.chat_id = chat_id
        self.subscription = self.create_subscription(
            String, "chabot_answer", self.listener_callback, 10
        )
        self.publisher_ = self.create_publisher(String, "telegram_input", 10)
        self.get_logger().info("Telegram Node está rodando e esperando por comandos...")

    def listener_callback(self, msg):
        self.get_logger().info(f'Telegram recebeu: "{msg}"')
        response = msg.data
        self.get_logger().info(f'Telegram retornou: "{response}"')

        response_msg = String()
        response_msg.data = response
        self.publisher_.publish(response_msg)



@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    texto = """
    Digite o nome do item que você deseja pedir:    
"""
    
    bot.send_message(mensagem.chat.id, texto)

    bot.register_next_step_handler(mensagem, processar_resposta)


def processar_resposta(mensagem):
    resposta_usuario = mensagem.text.lower()
    telegram_node_instance = TelegramNode(mensagem.chat.id)
    telegram_node_instance.listener_callback(String(data=resposta_usuario))

    bot.send_message(mensagem.chat.id, "Pedido de realizado com sucesso!")


def verify(msg):
    return True

@bot.message_handler(func=verify)
def answer(msg):

    texto = """
    Olá, eu sou o Bot do grupo BBB, no que posso te ajudar hoje?

    1) Fazer um pedido
    2) Cancelar um pedido
    3) Verificar status de um pedido
    4) Tirar dúvidas
    5) Lista de produtos

"""
    bot.register_next_step_handler(msg, processar_resposta)
    bot.reply_to(msg, texto)

def main(args=None):
    rclpy.init(args=args)

    try:
        bot.polling()
    except KeyboardInterrupt:
        pass
    finally:
        rclpy.shutdown()


if __name__ == "__main__":
    main()