def from_string_to_list(string: str, container: list) -> None:
    ls = [int(x) for x in string.split()]
    container += ls
    