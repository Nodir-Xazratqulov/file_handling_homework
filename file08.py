def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f=open(data, mode='r')
    s=f.read()
    son=[]
    # k=0
    for i in s:
        if i.isdigit():
            son.append(int(i))
    return max(son)
print(main('txt_file/data08.txt'))
# Read data from file