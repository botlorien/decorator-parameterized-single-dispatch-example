from parameterized import *

print(registry)

register()(f3)
print(registry)

register(active=False)(f2)
print(registry)