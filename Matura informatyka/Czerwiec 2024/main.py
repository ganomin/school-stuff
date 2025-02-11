# Zadanie 4.2.
def wynik4_2(input_file):
    # Zmienne
    client_list = []
    client_iteration = 1 # Liczymy komputery od 1
    existing_clients_count = 0

    # Odczyt
    with open(input_file, "r") as file:
        for client in file.readlines():
            # Domyślnie file.readlines wyrzuca string,
            # dlatego musimy przekonwertować zmienną na int,
            # by wykorzystać ją później w funkcji
            client = int(client)
            client_list.append(client)

    # Wybieramy komputer z największą liczbą
    max_client = max(client_list)

    # Komputery, które nie są odbiorcami żadnego pakietu
    while client_iteration != max_client:
        if client_iteration not in client_list:
            existing_clients_count += 1
        client_iteration += 1

    # Wynik
    print(existing_clients_count)

print("Zadanie 4.2.:")
print("Przykład:", end=' ')
wynik4_2("odbiorcy_przyklad.txt") # 3
print("Odpowiedź:", end=' ')
wynik4_2("odbiorcy.txt") # 395
print()

# Zadanie 4.3.
def do_round_4_3(packet_list, client_setting):
    # Notatki
    # packet_list -> runda "0", stałe, poszczególne numery pakietów
    # client_setting -> runda "1", stałe ustawienie wysyłania pakietów
    # current_client_setting -> runda "n"

    # Zmienne
    current_client_setting = list(packet_list)
    current_round = 1
    is_found = False

    # Wykonanie rundy
    while not is_found:
        # Zmienna pomocnicza do inkrementowania numeru obecnego pakietu
        # Wymagane jest to, ponieważ w packet_list, pakiety nie są poukładane
        # po kolei, tylko tak jak mają być wysłane
        n = 1

        # Przejście po każdym pakiecie w obecnej rundzie
        for packet in packet_list:
            # print(packet) # DEBUG: obecny numer pakietu
            current_client_setting[n - 1] = client_setting[packet - 1]

            # Szukanie wymaganego pakietu
            # Numer komputera ma się pokrywać z numerem pakietu
            if current_client_setting[n - 1] == n:
                print(current_round, n)
                is_found = True
                break

            # Przejście do następnego pakietu
            n += 1

        # Zapis obecnej rundy
        packet_list = list(current_client_setting)
        # print(current_client_setting) # DEBUG: obecne ustawienie rundy

        # Zakończenie rundy, rozpoczęcie kolejnej
        current_round += 1

def wynik4_3(input_file):
    # Zmienne
    packet_list = []
    client_setting = []

    # Odczyt
    with open(input_file, "r") as file:
        for client in file.readlines():
            # Domyślnie file.readlines wyrzuca string,
            # dlatego musimy przekonwertować zmienną na int,
            # by wykorzystać ją później w funkcji
            client = int(client)
            client_setting.append(client)

    # Pakiety
    for packet in range(max(client_setting)):
        packet_list.append(packet + 1) # Liczymy pakiety od 1

    # Debug
    # print("Numery pakietów", packet_list)
    # print("Ustawienie odbiorców", client_setting)

    # Wykonaj rundę, przekazując listę pakietów i ustawienie ich wysysłania
    do_round_4_3(packet_list, client_setting)

print("Zadanie 4.3.:")
print("Przykład:", end=' ')
wynik4_3("odbiorcy_przyklad.txt") # 3 7
print("Odpowiedź:", end=' ')
wynik4_3("odbiorcy.txt") # 3 346
print()

# Zadanie 4.4.
def do_round_4_4(packet_list, client_setting):
    # Notatki
    # packet_list -> runda "0", stałe, poszczególne numery pakietów
    # client_setting -> runda "1", stałe ustawienie wysyłania pakietów
    # current_client_setting -> runda "n"

    # Zmienne
    current_client_setting = list(packet_list)
    current_round = 1
    list_of_packets = {}

    # Wykonanie rundy
    while current_round != 9:
        # Zmienna pomocnicza do inkrementowania numeru obecnego pakietu
        # Wymagane jest to, ponieważ w packet_list, pakiety nie są poukładane
        # po kolei, tylko tak jak mają być wysłane
        n = 1

        # Przejście po każdym pakiecie w obecnej rundzie
        for packet in packet_list:
            # print(packet) # DEBUG: obecny numer pakietu
            current_client_setting[n - 1] = client_setting[packet - 1]

            # Przejście do następnego pakietu
            n += 1

        # Zapis obecnej rundy
        packet_list = list(current_client_setting)
        # print(current_client_setting) # DEBUG: obecne ustawienie rundy

        # Największe liczby pakietów
        if current_round == 1 or current_round == 2 or current_round == 4 or current_round == 8:
            for packet in packet_list:
                if packet in list_of_packets:
                    list_of_packets[packet] += 1
                else:
                    list_of_packets[packet] = 1
            print(max(list_of_packets.values()))
            list_of_packets.clear()

        # Zakończenie rundy, rozpoczęcie kolejnej
        current_round += 1

def wynik4_4(input_file):
    # Zmienne
    packet_list = []
    client_setting = []

    # Odczyt
    with open(input_file, "r") as file:
        for client in file.readlines():
            # Domyślnie file.readlines wyrzuca string,
            # dlatego musimy przekonwertować zmienną na int,
            # by wykorzystać ją później w funkcji
            client = int(client)
            client_setting.append(client)

    # Pakiety
    for packet in range(max(client_setting)):
        packet_list.append(packet + 1) # Liczymy pakiety od 1

    # Debug
    # print("Numery pakietów", packet_list)
    # print("Ustawienie odbiorców", client_setting)

    # Wykonaj rundę, przekazując listę pakietów i ustawienie ich wysysłania
    do_round_4_4(packet_list, client_setting)

print("Zadanie 4.4.:")
print("Przykład:", end=' ')
wynik4_4("odbiorcy_przyklad.txt") # 2 2 3 4
print("Odpowiedź:", end=' ')
wynik4_4("odbiorcy.txt") # 6 8 15 20
print()