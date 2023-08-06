import subprocess
import platform
import time

from watchdogman import config, logger

SYSTEM = platform.system()

def throttle(wait_time):
    """
    Decorator that will throttle a function so that it is called only once every wait_time seconds
    If it is called multiple times, will run only the first time.
    See the test_throttle.py file for examples
    """

    def decorator(function):
        def throttled(*args, **kwargs):
            def call_function():
                return function(*args, **kwargs)

            if time.time() - throttled._last_time_called >= float(wait_time):
                call_function()
                throttled._last_time_called = time.time()

        throttled._last_time_called = 0
        return throttled

    return decorator

@throttle(1)
def on_any_event(event):
    if ".watchdogman" in event.src_path:
        logger.log("reloading configuration", True)
        config.CONFIG = config.load_config()
        return

    if SYSTEM == "Darwin" or SYSTEM == "Linux":
        process = subprocess.Popen(config.CONFIG.command.split())
    elif SYSTEM == "Windows":
        process = subprocess.Popen(config.CONFIG.command.split(), shell=True)
    logger.log(f"running {config.CONFIG.command}", True)
    process.communicate()
