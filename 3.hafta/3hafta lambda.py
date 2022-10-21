"""""
lambda_fonk = lambda a: a + 10
print(lambda_fonk(5))
"""""
# çok parametreli lambda var aşağıda

topla = lambda a, b: a + b
def toplama(a, b):
    return a + b
print(toplama(3, 5))
print(topla(3, 5))
print(type(topla))
print(type(toplama))