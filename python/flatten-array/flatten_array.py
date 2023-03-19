
def flatten(iterable: list) -> list:
    flat_list: list = []

    def recur_flat(coll):
        if isinstance(coll, list):
            for item in coll:
                recur_flat(item)
        elif coll is not None:
            flat_list.append(coll)

    recur_flat(iterable)
    return flat_list
