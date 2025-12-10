import platform
import os
import sys

class Notifier:
    def __init__(self):
        self.os_name = platform.system()
        self.has_win10toast = False
        
        if self.os_name == "Windows":
            try:
                from win10toast import ToastNotifier
                self.toaster = ToastNotifier()
                self.has_win10toast = True
            except ImportError:
                print("Warning: win10toast not found. Windows notifications will be text-only.")

    def notify(self, title: str, message: str):
        """Send a desktop notification based on the OS."""
        print(f"\n[Term Notification] {title}: {message}") # Always print to stdout
        
        try:
            if self.os_name == "Darwin":  # macOS
                self._notify_macos(title, message)
            elif self.os_name == "Linux":
                self._notify_linux(title, message)
            elif self.os_name == "Windows":
                self._notify_windows(title, message)
        except Exception as e:
            print(f"Error sending notification: {e}")

    def _notify_macos(self, title: str, message: str):
        script = f'display notification "{message}" with title "{title}"'
        os.system(f"osascript -e '{script}'")

    def _notify_linux(self, title: str, message: str):
        os.system(f'notify-send "{title}" "{message}"')

    def _notify_windows(self, title: str, message: str):
        if self.has_win10toast:
            self.toaster.show_toast(title, message, duration=5, threaded=True)
