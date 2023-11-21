from rclpy.node import Node
from std_msgs.msg import String
import rclpy
from langchain.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableMap, RunnablePassthrough

class LlmNode(Node):
    def __init__(self, base_url, model_name):
        super().__init__("llm_node")
        self.subscription = self.create_subscription(
            String, "llm_command", self.listener_callback, 10
        )
        self.publisher_ = self.create_publisher(String, "llm_response", 10)
        self.ollama = Ollama(base_url=base_url, model=model_name)
        self.get_logger().info("LLM Node está rodando e esperando por comandos...")

    def run_ollama(self, text):
        try:
            ollama_response = ""
            for s in self.ollama.stream(text):
                ollama_response += s

            return ollama_response
        except Exception as exp:
            self.get_logger().info(exp)

    def listener_callback(self, msg):
        self.get_logger().info(f'LLM recebeu: "{msg.data}"')
        response = self.run_ollama(msg.data)
        self.get_logger().info(f'LLM retornou: "{response}"')

        response_msg = String()
        response_msg.data = response
        self.publisher_.publish(response_msg)


def main(args=None):
    rclpy.init(args=args)
    llm_node = LlmNode(
        base_url="http://localhost:11434",
        model_name="dolphin2.2-mistral",
    )

    try:
        rclpy.spin(llm_node)
    except KeyboardInterrupt:
        pass
    finally:
        llm_node.destroy_node()
        rclpy.shutdown()


if __name__ == "__main__":
    main()
