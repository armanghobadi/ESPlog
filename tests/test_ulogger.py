from ulogger.core import Logger


        
# Example Usage
logger = Logger(level="DEBUG", log_to_console=True, log_to_file=True, file_name="app_log.txt", max_file_size=1024, use_colors=True, log_format="text")

logger.debug("This is a debug message.")
logger.info("System initialized successfully.")
logger.warning("Warning: High memory usage detected.")
logger.error("Error: Disk space is running low.")
logger.critical("Critical error: Immediate action required.")
logger.trace("Trace message for detailed debugging.")

# Change log level
logger.set_level("ERROR")
logger.info("This message will not be logged.")
logger.error("A critical error occurred.")

# Disable logging
logger.disable()
logger.error("This message will not be logged.")

