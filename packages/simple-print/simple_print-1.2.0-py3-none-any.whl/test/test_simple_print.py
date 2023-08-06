from simple_print import sprint


def test_simple_print():
    
    for case in [1, "yoda", (1,), [1], {1: 1}, {1}, True, None, lambda x: x]:
        print("\n")
        print("*" * 30, type(case), "*" * 30)
        sprint(case)    
        sprint(case, c="red") # colors: grey, red, green, yellow, blue, magenta, cyan, white. 
        sprint(case, c="red", b="on_white") # backgrounds: on_grey, on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan
        sprint(case, c="blue", b="on_white", a="bold") # attributes: bold, dark, underline, blink, reverse, concealed
        sprint(f"master {case}", c="white", b="on_red", a="bold", s=True) # for f strings (any strings)
        sprint(case, c="red", b="on_white", a="bold", p=True) # with full path to file
        my_string = sprint(case, r=True) # return as string
        assert isinstance(my_string, str)
        print(my_string)
        my_string = sprint(case, r=True, p=True) # return as string with path
        assert isinstance(my_string, str)
        print(my_string)
        

