from num2words import num2words

def number_to_words(value: float, unit: str = "", decimals: int = 2) -> str:
    """
    Converts number to words based on rounded display value.
    """

    rounded_value = round(value, decimals)

    # If integer after rounding, remove decimal words
    if rounded_value.is_integer():
        words = num2words(int(rounded_value))
    else:
        words = num2words(rounded_value)

    words = words.replace("-", " ").title()

    if unit:
        return f"({words} {unit})"

    return f"({words})"