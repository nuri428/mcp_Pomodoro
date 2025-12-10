import argparse
import json
import os
from typing import Dict, Any

DEFAULT_CONFIG = {
    "focus_time": 25,
    "break_time": 5,
    "long_break_time": 15,
    "cycles": 4
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """Load configuration from a JSON file, returning defaults if file doesn't exist."""
    if not os.path.exists(config_path):
        return DEFAULT_CONFIG.copy()
    
    try:
        with open(config_path, 'r') as f:
            user_config = json.load(f)
            # Merge with defaults to ensure all keys exist
            config = DEFAULT_CONFIG.copy()
            config.update(user_config)
            
            # Migration support: if 'intervals' exists but 'cycles' doesn't, map it
            if "intervals" in config and "cycles" not in user_config:
                config["cycles"] = config.pop("intervals")
                
            return config
    except json.JSONDecodeError:
        print(f"Error parsing {config_path}. Using default configuration.")
        return DEFAULT_CONFIG.copy()

def get_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Pomodoro Timer (CLI)")
    
    parser.add_argument("--focus", type=int, help="Focus duration in minutes")
    parser.add_argument("--break", dest="break_time", type=int, help="Break duration in minutes")
    parser.add_argument("--long-break", type=int, help="Long break duration in minutes")
    parser.add_argument("--cycles", type=int, help="Number of cycles before long break")
    parser.add_argument("--config", type=str, default="config.json", help="Path to configuration file")
    
    return parser.parse_args()

def get_final_config() -> Dict[str, Any]:
    """Combine file config and CLI args (CLI args take precedence)."""
    args = get_args()
    config = load_config(args.config)
    
    if args.focus is not None:
        config["focus_time"] = args.focus
    if args.break_time is not None:
        config["break_time"] = args.break_time
    if args.long_break is not None:
        config["long_break_time"] = args.long_break
    if args.cycles is not None:
        config["cycles"] = args.cycles
        
    return config
