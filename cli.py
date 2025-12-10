#!/usr/bin/env python3
from pomodoro.config import get_final_config
from pomodoro.timer import PomodoroTimer

def main():
    config = get_final_config()
    
    print("Starting Pomodoro Timer with settings:")
    print(f"  Focus: {config['focus_time']}m")
    print(f"  Break: {config['break_time']}m")
    print(f"  Long Break: {config['long_break_time']}m")
    print(f"  Cycles: {config['cycles']}")
    print("\nPress Enter to start...", end="")
    input()
    
    timer = PomodoroTimer(config)
    timer.start()

if __name__ == "__main__":
    main()
