def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f=open(data, mode='r')
    s=f.read()
    son=[]
    for i in s.split('\n'):
        leen=len(i)
        son.append(leen)
        # if leen>max_lenght:
        #     max_lenght=leen 
    return son
print(main('txt_file/data06.txt'))
    
# Read data from file