'''
number of elements = (((stop - 1) - start) // step) + 1

ceil(x, y) = (x + y - 1) // y

Using formal stop:
    number of elements = ceil(stop-start, step) = ((stop-start) + step - 1) // step

Using actual stop:
    number of elements = ((stop - 1 - start) // step) + 1  = (stop - 1 - start + step) // step

max(0, ceil):
    This is to account for cases where start and stop are going in the oposite direction that that of the step (ceil < 0)

'''