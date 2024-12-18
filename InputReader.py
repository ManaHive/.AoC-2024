# using numpy io for reading the inputs, no need for this...
def get_real(n):
    with open(f'day{n}/input.txt') as i:
        input_nl = i.readlines()
    return [l.strip('\n\r') for l in input_nl]

def get_test(n):
    with open(f'day{n}/test_input.txt') as i:
        input_nl = i.readlines()
    return [l.strip('\n\r') for l in input_nl]