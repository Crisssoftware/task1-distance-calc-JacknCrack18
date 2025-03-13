import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from turtlesim.msg import Pose

class Pub_Sub(Node):

    def __init__(self):
        super().__init__('subscriber')
        self.subscription = self.create_subscription(Pose,'/turtle1/pose', self.listener_callback, 10)

        self.publisher_ = self.create_publisher(String, '/turtle1/distance_from_origin', 10)

    def listener_callback(self, msg):
        distance = (msg.x**2 + msg.y**2)**0.5

        msg = String()
        msg.data = "Distance is {}".format(distance)
        self.publisher_.publish(msg)
        self.get_logger().info("Publish: {}".format(msg.data))


def main(args=None):
    rclpy.init(args=args)

    pub_sub = Pub_Sub()

    rclpy.spin(pub_sub)

    pub_sub.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
