def evenNumberGenerator():
    for i in range(2,100,2):
        yield i
if __name__ == '__main__':
    value=evenNumberGenerator()
    for i in value:
        print(i)