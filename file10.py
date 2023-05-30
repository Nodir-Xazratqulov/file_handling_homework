def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f=open(data, mode='r')
    s=f.read()
    max_length=0
    for i in s.split('\n'):
        print(i)
        row_length=len(i)
        if row_length>max_length:
            max_length=row_length
    return  max_length
print(main('txt_file/data10.txt'))

