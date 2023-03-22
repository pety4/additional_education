def evenNumberGenerator(start,end):
    for i in range(start,end+2,2):
        yield i
if __name__ == '__main__':
    value=evenNumberGenerator(2,100)
    for i in value:
        print(i)