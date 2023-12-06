import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import re
import json
    
class RegexNode(Node):
    def __init__(self, intents):
        super().__init__('chatbot_node')
        self.publisher_ = self.create_publisher(String, 'move_robot', 10)
        self.telegram_publisher = self.create_publisher(String, 'telegram_message', 10)
        self.subscription = self.create_subscription(
            String,
            'llm_response',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.intents = intents

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
                x = float(match.group(1))
                y = float(match.group(2))
                tool_intention = True
                break
        
        if tool_intention and x and y:
            msg_data_dict = json.loads(msg.data)
            msg_data_dict['llm_response'] = 'Sua solicitação está sendo processada pelo robô.'
            msg_data_json = json.dumps(msg_data_dict)
            self.telegram_publisher.publish(String(data=msg_data_json))
            self.move_robot(x, y)
        else:
            self.telegram_publisher.publish(String(data=msg.data))

def main(args=None):
    rclpy.init(args=args)

    intents = {
        "tool_request": [
            # r"\(x:(\d+)\), \(y:(\d+)\)",
            r"\(x:(\d+\.\d+)\), \(y:(\d+\.\d+)\)",
            r"\(x:(\d+\.\d*)\), \(y:(\d+\.\d*)\)",
            r"\[\(x:(\d+\.\d*)\), \(y:(\d+\.\d*)\)\]"
            # Outras variações podem ser adicionadas aqui
        ],
    }

    chatbot_node = RegexNode(intents)

    try:
        rclpy.spin(chatbot_node)
    except KeyboardInterrupt:
        pass
    finally:
        chatbot_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
