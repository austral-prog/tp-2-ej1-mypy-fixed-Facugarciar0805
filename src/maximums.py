def max_of_two(x :int, y :int) -> int:

    if x >= y:
        return x
    else:
        return y

# Replace the "ANSWER HERE" for your answer
def max_of_three(x: int, y: int, z: int) -> int:
    return max_of_two(x,max(y,z))
