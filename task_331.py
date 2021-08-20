

def quadratic_sum(n):
    for i in range(int(n**0.5)):
        for j in range(i, int(n**0.5)):
            for k in range(j, int(n**0.5)):
                if i**2 + j**2 + k**2 == n:
                    yield i, j, k


if __name__ == "__main__":
    print(set(quadratic_sum(1)))
