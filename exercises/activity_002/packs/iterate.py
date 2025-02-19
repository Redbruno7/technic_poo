def menu():
    print('=' * 80)
    print('Menu:'.center(80))
    print('=' * 80)
    print('1. Register vehicle.')
    print('2. Modify register.')
    print('3. Delete register.')
    print('4. Show registers.')
    print('5. Exit.')
    print('-' * 80)

    while True:
        try:
            option = input('Choose option (1-5): ')
            if option.isdigit():
                option = int(option)

                if option == 1:
                    print('=' * 80)
                    print()
                    especify_menu()

                elif option == 2:
                    print('=' * 80)
                    print()
                    especify_menu()

                elif option == 3:
                    print('=' * 80)
                    print()
                    especify_menu()

                elif option == 4:
                    print('=' * 80)
                    print()
                    especify_menu()

                elif option == 5:
                    print('=' * 80)
                    print()
                    print('=' * 80)
                    print('Shutting down system.')
                    print('=' * 80)
                    print()
                    break

                else:
                    print('-' * 80)
                    print('Invalid option. Try again.')
                    print('-' * 80)

            else:
                print('-' * 80)
                print('Invalid option. Try again.')
                print('-' * 80)
        except ValueError:
            print('-' * 80)
            print('Invalid option. Try again.')
            print('-' * 80)

def especify_menu():
    print('=' * 80)
    print('Especify Menu:'.center(80))
    print('=' * 80)
    print('1. Car.')
    print('2. Motorcycle.')
    print('3. Truck.')
    print('4. Back.')
    print('-' * 80)

    while True:
        try:
            option = input('Choose option (1-4): ')
            if option.isdigit():
                option = int(option)

            else:
                print('-' * 80)
                print('Invalid option. Try again.')
                print('-' * 80)
        except ValueError:
            print('-' * 80)
            print('Invalid option. Try again.')
            print('-' * 80)