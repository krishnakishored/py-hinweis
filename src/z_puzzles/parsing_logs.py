from typing import List


def summarize_word_counts_by_category(lines: List[str], stopwords: List[str]):
    """
    Parses each line to extract category and words, then counts word frequency per category.

    :param lines: List of sentences with format '<category>: <sentence>'
    :param stopwords: Optional list of stopwords to ignore
    :return: Nested dictionary of word frequencies by category
    """

    from collections import Counter, defaultdict

    summary = defaultdict(Counter)
    # summary = {}

    # line = "error: failed to connect to database"
    for line in lines:
        ## remove stopwords and convert to list of words
        k, v = line.split(": ", 1)
        v_non_stop = [word for word in v.split(" ") if word not in stopwords]
        summary[k].update(v_non_stop)
    return {k: dict(v) for k, v in summary.items()}


def summarize_word_counts_by_category_without_using_collections(
    lines: List[str], stopwords: List[str]
):
    # Initialize empty dictionary for categories
    summary = {}

    for line in lines:
        # Split into category and words
        k, v = line.split(": ", 1)
        # Filter out stopwords
        v_non_stop = [word for word in v.split(" ") if word not in stopwords]

        # Initialize category dict if not exists
        if k not in summary:
            summary[k] = {}

        # Count words in this line
        for word in v_non_stop:
            summary[k][word] = summary[k].get(word, 0) + 1

    return summary


if __name__ == "__main__":
    lines = [
        "error: failed to connect to database",
        "info: user logged in successfully",
        "warning: disk space running low",
        "error: timeout during request",
        "info: job completed",
        "error: failed to connect to database",
    ]
    stopwords = ["to", "the", "and", "in", "during"]

    result = summarize_word_counts_by_category(lines, stopwords)
    print(result)

    # line = "error: failed connect database"
    # pair = line.split(":", 1)
    # print(pair)

# Expected output:
# {
#     "error": {"failed": 2, "connect": 2, "database": 2, "timeout": 1, "request": 1},
#     "info": {"user": 1, "logged": 1, "successfully": 1, "job": 1, "completed": 1},
#     "warning": {"disk": 1, "space": 1, "running": 1, "low": 1}
# }
