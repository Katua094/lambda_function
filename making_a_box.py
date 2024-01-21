# def loud(text):
#     return text.upper()
# def queit(text):
#     return text.lower()
# def hello(func):
#     x=func("calvin")
#     print(x)

# hello(queit)
# hello(loud)

def divisor(x):
    def dividend(y):
        return y/x
    return dividend

divide=divisor(4)
print(divide(200))


