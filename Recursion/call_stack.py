def funcThree():    # this func gets popped off first
    print('Three')

def funcTwo():
    funcThree()
    print('Two')

def funcOne():
    funcTwo()       # Calling another function
    print('One')

funcOne()