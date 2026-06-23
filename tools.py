from langchain. tools import tool

@tool
def calculator(expression: str) -> str:
    """Perform mathematical calculations. """
    try:
        return str(eval(expression))
    except:
        return "Invalid Expression"


@tool
def word_counter(text: str) -> str:
    """Count the number of words in the given text. """
    return f"Total words: {len(text.split())}"