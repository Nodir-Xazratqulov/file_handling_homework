def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    
    f=open(data,mode='r')
    a=f.read()
    s=[]
    d=[]
    k=0
    j=0
    for i in a:
        if i.isdigit():
            k+=1
        elif i.isalpha():
            j+=1
    s.append(k)
    d.append(j)

    
    return s+d
print(main('txt_file/data05.txt'))


# Read data from file