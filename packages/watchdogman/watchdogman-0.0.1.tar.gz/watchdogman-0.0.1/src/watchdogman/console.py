from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
from os.path import exists, join
import time
import argparse
from watchdogman import config, logger
from .event import on_any_event

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", help="Directory to watch")
    parser.add_argument("-a", "--allow", help="JSON list of file patterns to allow")
    parser.add_argument("-i", "--ignore", help="JSON list of file patterns to ignore")
    parser.add_argument("-f", "--ignore_directories", action="store_true", default=False, help="JSON list of file patterns to ignore")
    parser.add_argument("-c", "--command", help="Command to run on file change")
    args = parser.parse_args()

    if exists(join("./", ".watchdogman")):
        config.CONFIG = config.load_config()
    else:
        config.CONFIG = config.Config(args.directory, args.allow, args.ignore, args.ignore_dirs, args.command)

    event_handler = PatternMatchingEventHandler(
        config.CONFIG.allow_patterns,
        config.CONFIG.ignore_patterns,
        config.CONFIG.ignore_dirs,
    )
    logger.log(f"watching directory: {config.CONFIG.directory}")
    logger.log(f"allow patterns: {config.CONFIG.allow_patterns}")
    logger.log(f"ignore patterns: {config.CONFIG.ignore_patterns}")
    logger.log(f"ignore directories: {config.CONFIG.ignore_dirs}")
   
    event_handler.on_any_event = on_any_event

    observer = Observer()
    observer.schedule(event_handler, config.CONFIG.directory, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    main()
    