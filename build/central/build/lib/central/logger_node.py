import os
from datetime import datetime

import rclpy
from ament_index_python.packages import get_package_share_directory
from rclpy.node import Node
from std_msgs.msg import String

class LoggerNode(Node):
    def __init__(self, data_file_path):
        super().__init__("logger_node")
        # Configuração do ROS
        self.subscription = self.create_subscription(
            String, "log_register", self.listener_callback, 10
        )
        self.data_file_path = data_file_path
        self.get_logger().info("Logger Node está rodando e registrando informações")

    def listener_callback(self, msg):
        self.get_logger().info(f'Registrando log: "{msg.data}"')

        # Pegando o tempo e input no LLM
        time_input = datetime.now()
        # os.makedirs(os.path.dirname(self.data_file_path), exist_ok=True)

        with open(self.data_file_path, "a") as log_file:
            try:
                log_file.write(f"{msg.data} | {time_input}\n")  # Ensure a new line after each entry
            except Exception as e:
                self.get_logger().error(f"Error writing to file: {str(e)}")

def main(args=None):
    rclpy.init(args=args)

    # Nome do seu pacote
    package_name = 'central'

    # Construa o caminho para o diretório de compartilhamento do pacote
    package_share_directory = get_package_share_directory(package_name)

    # Construa o caminho para o seu arquivo de dados dentro do diretório de recursos
    data_file_path = os.path.join(package_share_directory, 'resource', 'logs.txt')

    logger_node = LoggerNode(data_file_path=data_file_path)
    try:
        rclpy.spin(logger_node)
    except KeyboardInterrupt:
        pass
    finally:
        logger_node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
