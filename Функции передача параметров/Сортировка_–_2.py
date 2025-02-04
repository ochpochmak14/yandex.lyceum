def sorting_bis(key: str, reverse: bool) -> None:
    if key == "len":
        data.sort(key=len, reverse=reverse)
    else:
        data.sort(reverse=reverse)