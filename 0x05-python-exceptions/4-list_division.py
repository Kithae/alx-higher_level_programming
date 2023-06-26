#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []
    div_temp = 0
    for a in range(0, list_length):
        try:
            div_temp = my_list_1[a] / my_list_2[a]
        except TypeError:
            div_temp = 0
            print("wrong type")
        except ZeroDivisionError:
            div_temp = 0
            print("division by 0")
        except IndexError:
            div_temp = 0
            print("out of range")
        finally:
            pass
        res.append(div_temp)
    return res
