def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f=open(data, mode='r')
    s=f.read()
    return len(s)
print(main('txt_file/data02.txt'))
# Read data from file