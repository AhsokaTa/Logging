import logging

logging.basicConfig(filename='error_file.log', level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def division(numerator, denominator):
    try:
        result = numerator / denominator
        return result
    except ZeroDivisionError as e:        
        logging.error(f"Division by zero {e}", exc_info=True)
        raise
    except Exception as e:       
        logging.error(f"unexpected error: {e}", exc_info=True)
        raise

numerator = 10
denominator = 0  

try:
    result = division(numerator, denominator)
except Exception as e:    
    logging.error(f"division error: {e}", exc_info=True)
    print("An error occurred during the division")


