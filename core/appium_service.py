import subprocess
import time
import socket
import shutil


class AppiumService:

    def __init__(self, host="127.0.0.1", port=4723):
        self.host = host
        self.port = port
        self.process = None
        self.appium_cmd = shutil.which("appium")

    def start(self):
        if self._is_running():
            return

        self.process = subprocess.Popen(
            [
                self.appium_cmd,
                "-a", self.host,
                "-p", str(self.port),
                "--log", "logs/appium.log",
                "--allow-insecure",
                "*:chromedriver_autodownload"
            ]
        )

        self._wait_until_running()

    def stop(self):
        if self.process:
            subprocess.run(
                ["taskkill", "/F", "/T", "/PID", str(self.process.pid)],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

    def _is_running(self):
        try:
            with socket.create_connection((self.host, self.port), timeout=2):
                return True
        except OSError:
            return False

    def _wait_until_running(self, timeout=30):
        start = time.time()
        while time.time() - start < timeout:
            if self._is_running():
                return
            time.sleep(1)
        raise RuntimeError("Appium did not start")
