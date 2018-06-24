import socket
import time

socket_receive_buffer = 4096


class OpensyslogSyslog:
    def __init__(self, opensysloghelper):
        self.helper = opensysloghelper

    def monitor(self):
        self.helper.print(self.helper.log_level_debug, "OpensyslogSyslog:monitor(): enter")

        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.bind((self.helper.config["syslog"]["ip"], self.helper.config["syslog"]["port"]))
            while True:
                data, address = sock.recvfrom(socket_receive_buffer)
                self.handle_incoming_data(data.decode('utf-8'))
        except Exception as e:
            self.helper.print(self.helper.log_level_error, "OpensyslogSyslog:monitor():Exception: " + str(e))
            time.sleep(60)
        self.helper.print(self.helper.log_level_debug, "OpensyslogSyslog:monitor(): exit")

    def handle_incoming_data(self, string_data):
        self.helper.print(self.helper.log_level_debug, "OpensyslogSyslog:hid(): enter")

        self.helper.log_data(string_data)
        self.parse_message_data(string_data)

        self.helper.print(self.helper.log_level_debug, "OpensyslogSyslog:hid(): exit")

    def parse_message_data(self, string_data):
        self.helper.print(self.helper.log_level_debug, "OpensyslogSyslog:pmd(): enter")

        # Future implementation

        self.helper.print(self.helper.log_level_debug, "OpensyslogSyslog:pmd(): exit")
