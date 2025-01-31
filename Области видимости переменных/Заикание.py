last_message = ""
 
 
def print_without_duplicates(message: str) -> None:
    global last_message
    if message != last_message:
        print(message)
    last_message = message