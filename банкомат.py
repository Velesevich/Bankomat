def vvedikartu():
    print('вставьте карту: ')
    a=input('напишите ok')
    return(a)
def languadge():
    print('выберите язык/ change languadge: ')
    a=input()
    return(a)
def pin_ru():
    print('введите pin: ')
    a=input()
    return(a)
def operacia_ru():
    print('выберите операцию:\n'
          '1. просмотреть баланс'
          '2. снять деги ')
    a=input()
    return(a)
def izvlech_kartu_ru():
    print('извлеките карту: ')
    return()
def balance_ru():
    print('ваш баланс ')
    return()
def dengi_ru():
    print('введите сумму: ')
    return()
def neverno():
    print('неверный ввод ')

def pin_en():
    print('pin: ')
    return ()
def operacia_en():
    print('what do you want: ')
    return ()

def izvlech_kartu_en():
    print('del karta: ')
    return()
def balance_en():
    print('your balance: ')
    return()
def dengi_en():
    print('how mach: ')
    return()


def menedger():
    while vvedikartu() != 'ok':
        menedger()
    else:
        while True:
            a=languadge()
            if a == 'ru':
                while True:
                    a=pin_ru()
                    if a=='1234':
                        while True:
                            a=operacia_ru()
                            if a=='1':
                                balance_ru()
                            elif a=='2':
                                dengi_ru()
                            else:
                                neverno()
                        else:
                            neverno()
                    else:
                        neverno()


            elif a=='en':
                pin_en()
            else:
                neverno()




    return()

menedger()
