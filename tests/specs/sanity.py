import chefnife

import fork
import knife


if __name__ == '__main__':
    g = chefknife.Giraffe()
    f = fork.Fork(g)
    z = chefknife.Zebra()
    k = knife.Knife(z, f)
    