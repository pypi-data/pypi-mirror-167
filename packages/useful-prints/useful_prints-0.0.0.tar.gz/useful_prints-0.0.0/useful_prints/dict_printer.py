from varname import nameof
from colorful_terminal import *


def pretty_print_dict(
    dic: dict,
    print_dict_name: bool = True,
    do_ljust_keys: bool = True,
    colored: bool = True,
    name_rgb=(255, 175, 0),
    key_rgb=(0, 255, 255),
    value_rgb=(255, 255, 0),
    colon_rgb=(255, 255, 255),
    syntax_rgb=(200, 200, 200),
):
    if colored:
        n_color = Fore.rgb(*name_rgb)
        k_color = Fore.rgb(*key_rgb)
        dot_color = Fore.rgb(*colon_rgb)
        v_color = Fore.rgb(*value_rgb)
        s_color = Fore.rgb(*syntax_rgb)
        reset = Fore.RESET
    else:
        n_color = ""
        k_color = ""
        dot_color = ""
        v_color = ""
        reset = ""
        s_color = ""
    if print_dict_name:
        name = n_color + nameof(dic, frame=2) + reset + s_color + " = {\n" + reset
        spacer = "\t"
    else:
        name = ""
        spacer = ""
    len_dic = len(dic.items())
    max_k_len = 0
    if do_ljust_keys:
        for i, (k, v) in enumerate(dic.items()):
            k = repr(k)
            if len(k) > max_k_len:
                max_k_len = len(k)
    for i, (k, v) in enumerate(dic.items()):
        k, v = repr(k).ljust(max_k_len), repr(v)
        ink = f"{spacer}{k_color}{k}{dot_color}: {v_color}{v}{reset}"
        if i != len_dic - 1 and print_dict_name:
            ink += s_color + "," + reset
        name += ink + "\n"
    if print_dict_name:
        name += s_color + "}" + reset
    colored_print(name)


if __name__ == "__main__":

    test = "Das ist ein Test!"
    abc = "Das ist ein Test!"

    dic = {"a": 1, "b": 2, 3: "c"}

    pretty_print_dict(dic)
