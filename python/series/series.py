
def slices(series, length):
    if not series or length <= 0 or len(series) < length:
        raise ValueError("series cannot be empty / lenght must be greater that zero / \
                         len(series) must be equal or greater than length")

    return [series[i : (length + i)] for i in range(len(series) - length + 1)]

