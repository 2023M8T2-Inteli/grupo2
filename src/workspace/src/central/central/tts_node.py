import rclpy
from rclpy.node import Node
from openai import OpenAI
from std_msgs.msg import String
from io import BytesIO
from playsound import playsound
import time
from ament_index_python.packages import get_package_share_directory
import os

class TTSNode(Node):
    def __init__(self):
        super().__init__('tts_node')
        self.client = OpenAI()
        self.subscription = self.create_subscription(
            String,
            'move_robot',
            self.listener_callback,
            10)

    def generate_speech(self):
     #   response = self.client.audio.speech.create(
      #      model="tts-1",
       #     voice="alloy",
        #    input= text,
        #)
        

        package_name = 'central'

    # Construa o caminho para o diretório de compartilhamento do pacote
        package_share_directory = get_package_share_directory(package_name)

    # Construa o caminho para o seu arquivo de dados dentro do diretório de recursos
        data_file_path = os.path.join(package_share_directory, 'resource', 'audio.mp3')

        playsound(data_file_path)
        time.sleep(5)

    def listener_callback(self, msg):
        self.generate_speech(msg.data)
        self.get_logger().info(f"Received command: {msg.data}")

def main(args=None):

    rclpy.init(args=args)
    tts_node = TTSNode()

    try:
        rclpy.spin(tts_node)
    except Exception as e:
        tts_node.get_logger().error(f"Error: {e}")

    tts_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
