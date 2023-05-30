def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f=open(data, mode='r')
    s=f.read()
    k=0
    for i in s:
        if i.isdigit():
            k+=int(i)
    return k
print(main('txt_file/data07.txt'))
    
# Read data from file