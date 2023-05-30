def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """

    f=open(data, mode='r')
    
    s=f.read()
    a=s.split(',')
    list1 = []
    for i in a:
        i=int(i)
        list1.append(i)
    return (list1)


    file1 = open('myFile.txt', mode='w')
    w = file1.write(str(list1))
    # print(w)
    # return w


    

print(main("txt_file/data01.txt"))

# Read data from file






