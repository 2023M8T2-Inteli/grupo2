import telebot
from rclpy.node import Node
from std_msgs.msg import String
import rclpy
import threading
import os
from ament_index_python.packages import get_package_share_directory

class TelegramNode(Node):
    def __init__(self, api_key):
        super().__init__('telegram_node')
        self.bot = telebot.TeleBot(api_key)
        self.subscription = self.create_subscription(
            String, "llm_response", self.listener_callback, 10
        )
        self.publisher = self.create_publisher(String, "llm_command", 10)
        self.voice_publisher = self.create_publisher(String, "voice_command", 10)
        self.get_logger().info("Telegram Node is running and waiting for commands...")
        self.chat_id = None
        self.initialize_telegram_bot()

    def verify_message(self, message):
        return True

    def initialize_telegram_bot(self):

        @self.bot.message_handler(func=self.verify_message)
        def respond_to_message(message):
            intro_text = """
              Olá, eu sou o Bot do grupo BBB, no que posso te ajudar hoje?

- Fazer a requisicao de uma peça
- Perguntar sobre alguma peça
            """
            self.bot.register_next_step_handler(message, self.process_response)
            self.bot.reply_to(message, intro_text)

        # Run the bot polling in a separate thread
        polling_thread = threading.Thread(target=self.bot.polling)
        polling_thread.start()

    def process_response(self, message):

        self.get_logger().info("Mensagem chegou")
        self.get_logger().info(message.content_type)
        if message.content_type == 'voice':
            self.handle_voice_message(message)
        elif message.content_type == 'text':
            self.handle_text_message(message)

    def handle_text_message(self, message):
        user_response = message.text.lower()
        self.chat_id = message.chat.id
        self.publisher.publish(String(data=user_response))
        self.get_logger().info(f'LLM received: "{user_response}"')

    def handle_voice_message(self, message):
        # Obter informações do arquivo de voz
        file_info = self.bot.get_file(message.voice.file_id)

         # Encontre o diretório do pacote
        package_dir = get_package_share_directory('central')

        # Construa o caminho para o diretório 'resource/voice_files'
        voice_file_directory = os.path.join(package_dir, 'resource', 'voice_files')

        # Baixar o arquivo de voz
        downloaded_file = self.bot.download_file(file_info.file_path)
        voice_file_path = os.path.join(voice_file_directory, f'{file_info.file_id}.ogg')

        # Certifique-se de que o diretório existe
        os.makedirs(voice_file_directory, exist_ok=True)

        # Salve o arquivo de voz no diretório especificado
        with open(voice_file_path, 'wb') as new_file:
            new_file.write(downloaded_file)

        # Enviar o caminho do arquivo para o nó de processamento de voz
        self.publish_voice_file_path(voice_file_path)
    
    def publish_voice_file_path(self, file_path):
        self.voice_publisher.publish(String(data=file_path))
        self.get_logger().info(f'Voice file path sent to voice processing node: "{file_path}"')

    def listener_callback(self, msg):
        self.get_logger().info('Listener callback activated')
        response = msg.data
        self.get_logger().info(f'LLM sent: "{response}"')
        self.bot.send_message(self.chat_id, response)

def main(args=None):
    API_KEY = '6789925207:AAGWEl8dbtY3-C-EO3-g9gJQURvYQozIuaI'

    rclpy.init(args=args)

    try:
        telegram_node = TelegramNode(api_key=API_KEY)
        rclpy.spin(telegram_node)
    except KeyboardInterrupt:
        pass
    finally:
        rclpy.shutdown()

if __name__ == "__main__":
    main()
