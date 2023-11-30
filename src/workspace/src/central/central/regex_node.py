import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import re
    
class RegexNode(Node):
    def __init__(self, command_processor, intents, actions):
        super().__init__('chatbot_node')
        self.command_processor = command_processor
        self.publisher_ = self.create_publisher(String, 'move_robot', 10)
        self.subscription = self.create_subscription(
            String,
            'chat_commands',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.intents = intents
        self.actions = actions

        self.get_logger().info('RegexNode está rodando e esperando por comandos...')

    def move_robot(self, x, y):
        self.get_logger().info(f'Movendo o robô para a posição ({x}, {y})')

        navegation_message = {
            'x': x,
            'y': y,
        }
        navegation_message_json = json.dumps(navegation_message)
        self.publisher_.publish(String(data=navegation_message_json))


    def listener_callback(self, msg):
        self.get_logger().info(f'Recebi: "{msg.data}"')
        command = msg.data.lower().strip()
            
        tool_intention = False
        for pattern in self.intents['tool_request']:
            match = re.search(pattern, command)
            if match:
                x = int(match.group(1))
                y = int(match.group(2))
                tool_intention = True
                break
        
        if tool_intention and x and y:
            return self.move_robot(x, y)
        
        return "Desculpe, não entendi o comando."


def main(args=None):
    rclpy.init(args=args)

    intents = {
        "tool_request": [
            r"\(x:(\d+)\), \(y:(\d+)\)",
            # Outras variações podem ser adicionadas aqui
        ],
    }

    chatbot_node = RegexNode(command_processor, intents, actions)

    try:
        rclpy.spin(chatbot_node)
    except KeyboardInterrupt:
        pass
    finally:
        chatbot_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
