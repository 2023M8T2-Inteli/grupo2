import telebot
from rclpy.node import Node
from std_msgs.msg import String
import rclpy
import threading

class TelegramNode(Node):
    def __init__(self, chave_api):
        super().__init__('telegram_node')
        self.bot = telebot.TeleBot(chave_api)
        self.subscription = self.create_subscription(
            String, "llm_response", self.listener_callback, 10
        )
        self.publisher_ = self.create_publisher(String, "llm_command", 10)
        self.get_logger().info("Telegram Node está rodando e esperando por comandos...")
        self.chat_id = None
        self.init_telegram_bot()

    def verify(self, msg):
        return True

    def init_telegram_bot(self):

        @self.bot.message_handler(func=self.verify)
        def answer(msg):

            texto = """
            Olá, eu sou o Bot do grupo BBB, no que posso te ajudar hoje?

- Fazer a requisicao de uma peça
- Perguntar sobre alguma peça

            """
            self.bot.register_next_step_handler(msg, self.processar_resposta)
            self.bot.reply_to(msg, texto)

        # Executa o polling do bot em uma thread separada
        thread = threading.Thread(target=self.bot.polling)
        thread.start()

    def processar_resposta(self, mensagem):
        resposta_usuario = mensagem.text.lower()
        self.chat_id = mensagem.chat.id
        self.publisher_.publish(String(data=resposta_usuario))
        self.get_logger().info(f'LLM recebeu: "{resposta_usuario}"')

    def listener_callback(self, msg):
        self.get_logger().info(f'Listener callback ativado')
        response = msg.data
        self.get_logger().info(f'LLM enviou: "{response}"')
        self.bot.send_message(self.chat_id, response)

def main(args=None):
    CHAVE_API = '6789925207:AAGWEl8dbtY3-C-EO3-g9gJQURvYQozIuaI'

    rclpy.init(args=args)

    try:
        telegram_node = TelegramNode(chave_api=CHAVE_API)
        rclpy.spin(telegram_node)
    except KeyboardInterrupt:
        pass
    finally:
        rclpy.shutdown()

if __name__ == "__main__":
    main()
