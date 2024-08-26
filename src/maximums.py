def max_of_two(x :int, y :int) -> int:
    biggest:int = x
    if x >= y:
        return biggest
    else:
        biggest = y
        return biggest

# Replace the "ANSWER HERE" for your answer
def max_of_three(x, y, z) -> int:
    return max_of_two(x,max(y,z))
