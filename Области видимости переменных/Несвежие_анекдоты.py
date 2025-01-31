st = set()


def print_only_new(message: str) -> None:
    if message not in st:
        print(message)
        st.add(message)
    