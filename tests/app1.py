print('Hello Python!')

from operator import add, mul
from itermethodchain import IterMethodChain as imc

it = imc([1,2,3])
print(it)
print(
    imc([1,2,3])
    .map(lambda n: n * 2)
    .list()
    )
N=10
print(
    imc(range(N))
    .map(lambda n: n+1)
    .reduce(add)
)

print(
    imc(range(N))
    .map(lambda n: n+1)
    .filter(lambda n: n % 2 == 0)
    .list()
)

print(
    imc(range(N))
    .map(lambda n: n+1)
    .filter(lambda n: n % 2 == 0)
    .reduce(add)
)

print(
    imc(range(N))
    .map(lambda n: n+1)
    .reduce(mul)
)

print(
    imc(range(N))
    .map(lambda n: n+1)
#    .reduce(mul)
)