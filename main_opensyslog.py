import sys

from opensyslog_helper import OpensyslogHelper
from opensyslog_syslog import OpensyslogSyslog


class OpensyslogMonitor:
    def __init__(self, config_folder):
        self.helper = OpensyslogHelper(config_folder)
        self.helper.print(self.helper.log_level_info, "OpensyslogMonitor: Starting Monitor")

        self.syslog = OpensyslogSyslog(self.helper)
        while True:
            try:
                self.helper.print(self.helper.log_level_debug, "OpensyslogMonitor: Start syslog monitor loop")
                self.syslog.monitor()
            except Exception as e:
                self.helper.print(self.helper.log_level_error, "OpensyslogMonitor: Exception: " + str(e))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        root_path = sys.argv[1]
        if not root_path.endswith("/"):
            root_path = root_path + "/"
    else:
        root_path = "/config/"
    print("Config folder: " + root_path)
    main_object = OpensyslogMonitor(root_path)
