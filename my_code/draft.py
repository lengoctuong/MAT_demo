ccm = 69

def a(fn):
    global ccm
    
    print('dmm lan', ccm)
    ccm += 1


@a
def b():
    pass

@a
def c():
    pass