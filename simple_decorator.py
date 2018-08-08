import random
import inspect

class KeyProvider(object):

    def __init__(self, f):
        self.f = f
        self.id = random.randint(1, 100000)

    def __call__(self, *args, **kwargs):
        print("Entering {} on {}".format( self.f.__name__, self.id))
        if 'myid' in inspect.getfullargspec(self.f).args:
            kwargs['myid'] = self.id
            print('injected to {}'.format(self.f.__name__))
        self.f(*args, **kwargs)
        print("Exited {} on {}".format( self.f.__name__, self.id))



@KeyProvider
def test1(name, myid=0):
    print("{} test 1 - {}".format(name, myid))


@KeyProvider
def test2(name):
    print("{} test 2".format(name))

if __name__ == "__main__":
    test1('Ray')
    test2('Ray')