#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            # Check if both elements are numbers
            if i >= len(my_list_1):
                raise IndexError("out of range")
            if i >= len(my_list_2):
                raise IndexError("out of range")
            
            el_1 = my_list_1[i]
            el_2 = my_list_2[i]
            
            if not isinstance(el_1, (int, float)) or not isinstance(el_2, (int, float)):
                raise TypeError("wrong type")
            
            # Perform the division
            result.append(el_1 / el_2)
        
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except TypeError:
            print("wrong type")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
        finally:
            pass

    return result

if __name__ == "__main__":
    my_l_1 = [10, 8, 4]
    my_l_2 = [2, 4, 4]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)

    print("--")

    my_l_1 = [10, 8, 4, 4]
    my_l_2 = [2, 0, "H", 2, 7]
    result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
    print(result)
