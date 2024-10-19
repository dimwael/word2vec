def fibonacci(n):
    """
    Calculate the nth Fibonacci number.
    
    Args:
        n (int): The position of the desired Fibonacci number.
        
    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
