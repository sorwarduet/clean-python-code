"""


"""
# Bad code
d = {}
d.update({1: 'one', 2: 'tow'})

# Good code

d.update([(3,'there'),(4,'four')])


def my_function():
    """" Return Computation"""
    return None

import string
import random

class Test:
    product_id = 'Hello'

    def id_generator(self, size=6, chars=string.ascii_uppercase + string.digits):
        print(chars)
        return ''.join(random.choice(chars) for _ in range(size))
    

    

obj=Test()

print(obj.id_generator())



