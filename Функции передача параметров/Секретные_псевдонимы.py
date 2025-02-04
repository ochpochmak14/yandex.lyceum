def secret_sort():
    secret_avatars.sort(key=lambda x: sum(1 for i in x[1::2].lower() if i in 'aeiouy'))