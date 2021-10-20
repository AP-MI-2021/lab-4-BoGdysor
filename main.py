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


def even_length(list_1, list_2):
    """
    Verifica daca cele doua liste au acelasi numar de elemente pare
    :param list_1: Lista cu numere intregi
    :param list_2: Lista cu numere intregi
    :return: 1 - Daca au acelasi numar de elemente pare, 0 - Daca nu au acelasi numar de elemente pare
    """
    even_count_1 = 0
    even_count_2 = 0
    for i in range(len(list_1)):
        if list_1[i] % 2 == 0:
            even_count_1 = even_count_1 + 1
    for i in range(len(list_2)):
        if list_2[i] % 2 == 0:
            even_count_2 = even_count_2 + 1
    if even_count_2 == even_count_1:
        return 1
    else:
        return 0


def test_even_length():
    assert even_length([10, 20, 30, 40], [2, 4, 6, 8]) == 1
    assert even_length([10, 2, 35, 41], [200, 400, 300, 500]) == 0
    assert even_length([1, 11, 111, 111], [2, 4, 6, 8]) == 0

def intersection(list_1,list_2):
    """
    
    :param list_1: 
    :param list_2: 
    :return: 
    """
    intersected_list = []
    for i in range(len(list_1)):
        for j in range(len(list_2)):
            if list_1[i] == list_2[j]:
                if list_1[i] not in intersected_list:
                    intersected_list.append(list_1[i])
    return intersected_list



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
            op = even_length(list_A, list_B)
            if op == 1:
                print("Listele au acelasi numar de elemente pare")
            else:
                print("Listele nu au acelasi numar de elemente pare")
        elif optiune == '3':
            inter_list = intersection(list_A,list_B)
            print(inter_list)
        elif optiune == '4':
            pass
        elif optiune == '5':
            pass
        elif optiune == 'x':
            break
        else:
            print("Optiune invalida!")


if __name__ == '__main__':
    test_even_length()
    main()
