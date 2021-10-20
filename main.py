




def read_list():
    """
    Citeste un string pe care il transforma intr-o lista de numere
    :return: lista de numere
    """
    str_list = input("Introduceti numerele pentru adaugarea in lista separate printr-o virgula: ")
    int_list = []
    str_list = str_list.split(" ")
    for i in str_list:
        int_list.append(int(i))
    return int_list


def main():
    list_A = []
    list_B = []
    while True:
        optiune = input("Introduceti optiunea:")
        if optiune == '1':
            print("introduceti prima lista:  ")
            list_A = read_list()
            print("Introucrti a 2a lista: ")
            list_B = read_list()
        elif optiune == '2':
            pass
        elif optiune == '3':
            pass
        elif optiune == '4':
            pass
        elif optiune == '5':
            pass


if __name__ == '__main__':
    main()
