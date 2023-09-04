import logging

def configure_logging():
    """
    Configure the logging system.

    This function sets up the logging system to write log messages to a file,
    with a specified log level, and a custom log message format.
    """
    logging.basicConfig(
        filename='error_file.log',  
        level=logging.DEBUG,        
        format='%(asctime)s - %(levelname)s - %(message)s'  
    )

def division(numerator, denominator):
    """
    Perform a division operation and handle exceptions.

    Args:
        numerator (float): The numerator for the division.
        denominator (float): The denominator for the division.

    Returns:
        float: The result of the division operation.

    Raises:
        ZeroDivisionError: If the denominator is zero.
    """
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError as e:
        logging.error(f"Division by zero: {e}", exc_info=True)
        raise
    except Exception as e:        
        logging.error(f"Unexpected error: {e}", exc_info=True)
        raise

if __name__ == "__main__":
    configure_logging()
    
    numerator = 10
    denominator = 0

    try:
        result = division(numerator, denominator)
    except Exception as e:
        # Handle the exception and log it
        logging.error(f"Division error: {e}", exc_info=True)
        print("An error occurred during the division")