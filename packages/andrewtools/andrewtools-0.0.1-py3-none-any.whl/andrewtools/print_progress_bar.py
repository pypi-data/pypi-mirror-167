"""Displays the progress of a loop with a command line progress bar"""
from utils.validate_input import validate_type


def print_progress_bar(
    iteration: int, total: int, width: int = 100, prefix: str = ""
) -> None:
    """
    Usage: Call as the first line inside of a loop.

    Note that the progress bar will not play well with your code if there are
    other print statements within the same loop.

    :param int iteration: the current iteration, 0-indexed
    :param int total: the total number of iterations, 1-indexed
    :param int width: the inner width of the progress bar itself [10-100]
    :param str prefix: a message to be printed on the left of the status bar
    """

    # Validate input types
    iteration = validate_type(iteration, int)
    total = validate_type(total, int)
    width = validate_type(width, int)
    prefix = validate_type(prefix, str)

    # Make sure width is in bounds
    if width < 10 or width > 100:
        raise ValueError("width must be an integer between 10 and 100, inclusive")

    # Make sure iteration and total in bounds
    if iteration < 0 or total < 0:
        raise ValueError("iteration and total must be positive integers")

    # Handle user error allowing iteration to be greater than or equal to total
    if iteration >= total:
        # It sure would suck if this tool to terminated a program that has been
        # running for a long time! Therefore, we will fail silently.
        msg = (
            " > Progress Bar error: iteration > total. "
            + "Note that iteration is 0-indexed and total is 1-indexed. "
            + "The loop will continue..."
        )
        print(msg, end="\r")
        return

    # Calculate percentage complete and create progress bar
    percent = (iteration + 1) / total
    complete = int(width * percent)
    bar = "*" * complete + "-" * (width - complete)
    print(f"\r{prefix} |{bar}| {percent * 100:.1f}%", end="\r")

    # Final iteration ends with newline character
    if percent == 1:
        print()


if __name__ == "__main__":

    # Usage
    import time

    iterations = 39
    for i in range(iterations):
        print_progress_bar(i, iterations, width=10, prefix="Progress")
        time.sleep(0.1)
