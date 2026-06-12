def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    D = {}
    for sentence in sentences:
        for word in sentence:
            if word not in D:
                D[word] = 0
            D[word] += 1
    return D