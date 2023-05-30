def main(data:str):
    """
    The data is from the file. Return the digits as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f=open(data, mode='r')
    s=f.read()
    # a=s.split(',')
    list1 = []
    for i in s:
        if i.isdigit():
            list1.append(str(i))
    return (list1)
print(main('txt_file/data03.txt'))
# Read data from file
