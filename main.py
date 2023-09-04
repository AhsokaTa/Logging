import logging

def configure_logging(log_file='error_file.log', log_level=logging.DEBUG):
    """
    Configure the logging system.

    Args:
        log_file (str): The name of the log file.
        log_level (int): The logging level (default is DEBUG).
    """
    logging.basicConfig(
        filename=log_file,
        level=log_level,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def safe_division(numerator, denominator):
    """
    Perform a division operation safely and handle exceptions.

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

def main():
    configure_logging(log_file='error_file.log', log_level=logging.DEBUG)
    
    numerator = 10
    denominator = 0

    try:
        result = safe_division(numerator, denominator)
    except Exception as e:
        logging.error(f"Division error: {e}", exc_info=True)
        print("An error occurred during the division")

if __name__ == "__main__":
    main()