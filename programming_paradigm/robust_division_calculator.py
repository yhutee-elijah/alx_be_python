def safe_divide(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return None
    
    if __name__ == "__main__":
        main()