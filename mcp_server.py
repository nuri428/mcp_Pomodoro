from mcp.server.fastmcp import FastMCP
from pomodoro.timer import PomodoroTimer
from pomodoro.config import get_final_config

mcp = FastMCP("pomodoro-mcp")

timer = PomodoroTimer(get_final_config())

@mcp.tool("get_status",
title="Get the current status of the timer",
description="Get the current status of the timer.")
def get_status():   
    return timer.get_status()

@mcp.tool("start_timer",
title="Start a pomodoro timer",
description="Start a pomodoro timer with the given settings.",
)
def start_timer(work: int, rest: int, cycles: int=1, long_break: int=0):
    timer.update_settings({"focus_time": work, "break_time": rest, "cycles": cycles, "long_break_time": long_break})
    timer.start()
    return {"message": "Timer started!"}

@mcp.tool("stop_timer",
title="Stop the timer",
description="Stop the timer.")
def stop_timer():
    timer.stop()
    return {"message": "Timer stopped!"} 

@mcp.tool("update_settings",
title="Update the settings of the timer",
description="Update the settings of the timer.")
def update_settings(work: int, rest: int, cycles: int=1, long_break: int=0):
    timer.update_settings({"focus_time": work, "break_time": rest, "cycles": cycles, "long_break_time": long_break})
    return {"message": "Settings updated!"}

if __name__ == "__main__":
    mcp.run()