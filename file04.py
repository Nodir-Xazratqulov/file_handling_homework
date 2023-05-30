def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f=open(data, mode='r')
    a=f.read()
    s=[]
    for i in a:
        if i.isalpha():
            s.append(str(i))
    s.insert(6,'\n')
    return s
print(main('txt_file/data04.txt'))
# Read data from file