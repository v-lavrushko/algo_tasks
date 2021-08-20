def smallestbin(n):
    s = f"{n:b}"
    return int(f'1{"0"*len(s)}', 2)


if __name__ == "__main__":
    print(smallestbin(15))