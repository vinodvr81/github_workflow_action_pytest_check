from typing import Callable

def my_type_dec(func: Callable) -> Callable:
    def my_type_add_upper(str1:str, str2:str):
        print("Before calling decorator {0}". format(func(str1, str2)))
        print("After Calling decorator {0}".format(str1.upper() + " " + str2.upper()))
        return "decorator call successful"
    return my_type_add_upper

@my_type_dec
def string_cap(str1:str, str2:str) -> str:
    return str1+" "+str2

if __name__ == '__main__':
    string_cap("hi", "vinod")