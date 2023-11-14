import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import re

class CommandProcessor:
    def __init__(self, intencoes, acoes):
        self.intencoes = intencoes
        self.acoes = acoes

    def processar_comando(self, comando):
        comando = comando.lower().strip()
        for intencao, padroes in self.intencoes.items():
            for padrao in padroes:
                match = re.match(padrao, comando, re.IGNORECASE)
                if match:
                    resposta = self.acoes[intencao](match.group(1))
                    return resposta
        return "Desculpe, não entendi o comando."

class ChatbotNode(Node):
    def __init__(self, command_processor):
        super().__init__('chatbot_node')
        self.command_processor = command_processor
        self.publisher_ = self.create_publisher(String, 'chat_responses', 10)
        self.subscription = self.create_subscription(
            String,
            'chat_commands',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        self.get_logger().info('ChatbotNode está rodando e esperando por comandos...')

    def listener_callback(self, msg):
        self.get_logger().info(f'Recebi: "{msg.data}"')
        response = self.command_processor.processar_comando(msg.data)
        self.get_logger().info(f'Respondendo: "{response}"')
        response_msg = String()
        response_msg.data = response
        self.publisher_.publish(response_msg)



def main(args=None):
    rclpy.init(args=args)

    intencoes = {
        "ir_para": [
            r"V[áa] para (?:o|a|os|as)? (.+)",
            r"V[áa] para (.+)",
            r"Dirija-se (?:ao|à|aos|às)? (.+)",
            r"Dirija-se para (?:o|a)? (.+)",
            r"Me leve para (?:o|a|os|as)? (.+)",
            r"Me leve (?:a|à)? (.+)",
            r"Quero ir (?:para|ao|à|aos|às|a)? (.+)",
            r"Por favor, me encaminhe (?:para|ao|à|a|aos|às)? (.+)",
            r"Pode me levar (?:para|ao|à|a|aos|às)? (.+)",
            r"Encaminhe-me (?:para|ao|à|aos|a|às)? (.+)",
            r"Quero ser levado (?:para|ao|à|a|aos|às)? (.+)",
            r"Leve-me at[eé] (?:o|a|os|as)? (.+)",
            r"Quero navegar (?:para|ao|à|aos|às)? (.+)",
            r"Desloque-se (?:para|ao|à|aos|às)? (.+)",
            r"Preciso ir (?:para|ao|à|aos|às|a)? (.+)",
            # Outras variações podem ser adicionadas aqui
        ],
    }

    # Dicionário de ações que relaciona intenções a funções
    acoes = {
        "ir_para": lambda lugar: f"Iniciando navegação para {lugar}"
    }
    
    command_processor = CommandProcessor(intencoes, acoes)
    chatbot_node = ChatbotNode(command_processor)

    try:
        rclpy.spin(chatbot_node)
    except KeyboardInterrupt:
        pass
    finally:
        chatbot_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
