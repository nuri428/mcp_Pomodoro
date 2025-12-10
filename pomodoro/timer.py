import time
import sys
from .notifier import Notifier
from .utils import clear_screen, format_time

class PomodoroTimer:
    def __init__(self, config: dict):
        self.config = config
        self.notifier = Notifier()

        self.focus_time = config["focus_time"] * 60
        self.break_time = config["break_time"] * 60
        self.long_break_time = config["long_break_time"] * 60
        self.cycles = config["cycles"]

        self.completed_cycles = 0

        # ------ Timer State for MCP ------
        self.is_running = False
        self.current_label = None
        self.remaining_seconds = 0
        # ----------------------------------

    def update_settings(self, config: dict):
        self.config = config
        self.focus_time = config["focus_time"] * 60
        self.break_time = config["break_time"] * 60
        self.long_break_time = config["long_break_time"] * 60
        self.cycles = config["cycles"]
        self.stop()

    def stop(self):
        self.is_running = False

    def start(self):
        try:
            while True:
                if not self.is_running:
                    self.run_break()
                    break

                self.run_focus_session()
                self.completed_cycles += 1

                if self.completed_cycles % self.cycles == 0:
                    self.run_long_break()
                else:
                    self.run_break()

        except KeyboardInterrupt:
            print("\n\nTimer stopped by user. Goodbye!")
            self.is_running = False
            sys.exit(0)

    def run_focus_session(self):
        self.current_label = f"FOCUS (Session {self.completed_cycles + 1})"
        self.notifier.notify("Pomodoro", "Focus time started! Let's work.")
        self._countdown(self.focus_time)
        self.notifier.notify("Pomodoro", "Focus session complete!")

    def run_break(self):
        self.current_label = "BREAK"
        self.notifier.notify("Pomodoro", "Time for a break!")
        self._countdown(self.break_time)
        self.notifier.notify("Pomodoro", "Break over. Ready to focus?")

    def run_long_break(self):
        self.current_label = "LONG BREAK"
        self.notifier.notify("Pomodoro", "Time for a long break!")
        self._countdown(self.long_break_time)
        self.notifier.notify("Pomodoro", "Long break over. Back to work!")

    def _countdown(self, duration: int):
        self.is_running = True
        self.remaining_seconds = duration

        while self.remaining_seconds > 0:
            clear_screen()
            print(f"[{self.current_label}]")
            print(f"Time Remaining: {format_time(self.remaining_seconds)}")
            print("\nPress Ctrl+C to stop.")

            time.sleep(1)
            self.remaining_seconds -= 1

        clear_screen()
        print(f"[{self.current_label}] Finished!")
        self.is_running = False

    # ------------- MCP-friendly method -------------
    def get_status(self):
        return {
            "is_running": self.is_running,
            "current_phase": self.current_label,
            "remaining_seconds": self.remaining_seconds,
            "completed_cycles": self.completed_cycles,
        }