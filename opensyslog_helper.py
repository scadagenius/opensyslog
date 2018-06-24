import datetime
import os
import yaml  # this needs package called PyYAML


class OpensyslogHelper:
    log_level_debug = 1
    log_level_info = 2
    log_level_warning = 3
    log_level_error = 4
    log_level_critical = 5

    def __init__(self, config_folder):
        self.config_folder = config_folder
        self.config = yaml.load(open(self.config_folder + 'config.yaml'))

        self.log_level = 2
        if self.config["syslog"]["logs"]["level"] == "debug":
            self.log_level = 1
        elif self.config["syslog"]["logs"]["level"] == "info":
            self.log_level = 2
        elif self.config["syslog"]["logs"]["level"] == "warning":
            self.log_level = 3
        elif self.config["syslog"]["logs"]["level"] == "error":
            self.log_level = 4
        elif self.config["syslog"]["logs"]["level"] == "critical":
            self.log_level = 5

        self.log_folder = self.config_folder + "logs/"
        self.syslog_log = self.log_folder + self.config["syslog"]["logs"]["syslog_log"]
        self.monitor_log = self.log_folder + self.config["syslog"]["logs"]["monitor_log"]

        if not os.path.exists(self.log_folder):
            os.makedirs(self.config_folder + "logs")
            self.print(self.log_level_info, "OpensyslogHelper:__init__(): Creating folder: " + self.log_folder)

    def get_log_level_to_string(self, log_level):
        log_level_str = ": "
        if log_level == self.log_level_debug:
            log_level_str = ":debug: "
        elif log_level == self.log_level_info:
            log_level_str = ":info: "
        elif log_level == self.log_level_warning:
            log_level_str = ":warn: "
        elif log_level == self.log_level_error:
            log_level_str = ":error: "
        elif log_level == self.log_level_critical:
            log_level_str = ":critical: "
        return log_level_str

    def log_data(self, message_data):
        self.print(self.log_level_debug, "OpensyslogHelper:ld(): enter")
        try:
            log_file_name = self.syslog_log + "-" + datetime.datetime.now().strftime('%Y-%m-%d') + ".log"
            log_str = ""
            if self.config["syslog"]["logs"]["prepend_timestamp"] == "true":
                log_str = datetime.datetime.now().strftime('%H:%M:%S') + "::: "
            log_str = log_str + message_data
            if self.config["syslog"]["logs"]["append_new_line"] == "true":
                log_str = log_str + "\n"
            with open(log_file_name, "a") as log_file:
                log_file.write(log_str)
        except Exception as e:
            self.print(self.log_level_error, "ErxHelper:log_data():Exception:" + str(e))
        self.print(self.log_level_debug, "OpensyslogHelper:ld(): exit")

    def print(self, log_level, str_print):
        if self.log_level > log_level:
            return
        try:
            log_file_name = self.monitor_log + "-" + datetime.datetime.now().strftime('%Y-%m-%d') + ".log"
            log_str = datetime.datetime.now().strftime('%H:%M:%S.%f')[:-3] + \
                      self.get_log_level_to_string(log_level) + str_print

            print(log_str)
            with open(log_file_name, "a") as log_file:
                log_file.write(log_str + "\n")
        except Exception as e:
            print(datetime.datetime.now().strftime('%H:%M:%S.%f')[:-3] + " : OpensyslogHelper:print():Exception: " +
                  str(e))
