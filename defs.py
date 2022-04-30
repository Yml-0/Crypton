import os
import sys
import base64
import perem
import default
import err
text=''
result_cesar=''

# Название утилиты
def name():
    os.system('cls')
    print('')
    for i in [perem.name1, perem.name2, perem.name3, perem.name4, perem.name5, perem.name6]:
        print(i)
    print('')

# Шифратор (Энкриптор)
def encrypt():
    operation = 'Encrypt'
    print('Do you want to change encrypt keys?')
    print('1 No (default)')
    print('2 Yes (possible errors)')
    change_keys = int(input())
    if change_keys == 1:
        crypt_key1 = 9 #Переменная шифра 1
        crypt_key2 = 5 #Переменная шифра 2
        crypt_key3 = 12 #Переменная шифра 3
        crypt_key4 = 27 #Переменная шифра 3
        crypt_key5 = 15 #Переменная шифра 3
        easy = 'CPK' 
        medium = 'QN4'
        hard = 'TQZ'
        key = 'Default'
        crypt_key1_show = key
        crypt_key2_show = key
        crypt_key3_show = key
        crypt_key4_show = key
        crypt_key5_show = key
        pref_show = key
    elif change_keys == 2:
        crypt_key1 = input('Key 1 (only the number): ') #Переменная шифра 1
        crypt_key2 = input('Key 2 (only the number): ') #Переменная шифра 2
        crypt_key3 = input('Key 3 (only the number): ') #Переменная шифра 3
        crypt_key4 = input('Key 4 (only the number): ') #Переменная шифра 4
        crypt_key5 = input('Key 5 (only the number): ') #Переменная шифра 5
        easy = 'CPK' 
        medium = 'QN4'
        hard = 'TQZ'
        key = 'Custom'
        crypt_key1_show = crypt_key1
        crypt_key2_show = crypt_key2
        crypt_key3_show = crypt_key3
        crypt_key4_show = crypt_key4
        crypt_key5_show = crypt_key5
    print('What do you want to encrypt?')
    text = input()
    how_long_text = int(len(text))
    result_cesar = ''
    result_cesar_base64 = ''
    result_cesar_base64_2 = ''
    for i in range(how_long_text):
        b=str(ord(text[i])+crypt_key1*crypt_key2+crypt_key3)
        result_cesar+=b+perem.space
    message = result_cesar
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    how_long_base64 = int(len(base64_message))
    for i in range(how_long_base64):
        b=str(ord(base64_message[i])+crypt_key1+crypt_key2*crypt_key3)
        result_cesar_base64+=b+perem.space
    # Перевод в base64
    message = result_cesar_base64
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message2 = base64_bytes.decode('ascii')
    # Перевод в win коды
    how_long_base64_3 = int(len(base64_message2))
    for i in range(how_long_base64_3):
        b=str(ord(base64_message2[i])+crypt_key4*4-crypt_key5*5)
        result_cesar_base64_2+=b+perem.space
    # Перевод в base64
    message = result_cesar_base64_2
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message3 = base64_bytes.decode('ascii')
    print('Very hard, but long encryption:')
    print(hard+base64_message3)
    print('Hard and short encryption:')
    print(medium+base64_message2)

# Шифратор (Энкриптор)
def decrypt():
    print('Do you want to change decrypt keys?')
    print('1 No (default)')
    print('2 Yes (possible errors)')
    change_keys = int(input())
    if change_keys == 1:
        crypt_key1 = 9 #Переменная шифра 1
        crypt_key2 = 5 #Переменная шифра 2
        crypt_key3 = 12 #Переменная шифра 3
        crypt_key4 = 27 #Переменная шифра 4
        crypt_key5 = 15 #Переменная шифра 5
        easy = 'CPK' 
        medium = 'QN4'
        hard = 'TQZ'
        key = 'Default'
        crypt_key1_show = key
        crypt_key2_show = key
        crypt_key3_show = key
        crypt_key4_show = key
        crypt_key5_show = key
        pref_show = key
    elif change_keys == 2:
        crypt_key1 = int(input('Key 1 (only the number): ')) #Переменная шифра 1
        crypt_key2 = int(input('Key 2 (only the number): ')) #Переменная шифра 2
        crypt_key3 = int(input('Key 3 (only the number): ')) #Переменная шифра 3
        crypt_key4 = int(input('Key 4 (only the number): ')) #Переменная шифра 4
        crypt_key5 = int(input('Key 5 (only the number): ')) #Переменная шифра 5
        easy = 'CPK' 
        medium = 'QN4'
        hard = 'TQZ'
        key = 'Custom'
        crypt_key_show = crypt_key1
        crypt_key2_show = crypt_key2
        crypt_key3_show = crypt_key3
        crypt_key4_show = crypt_key4
        crypt_key5_show = crypt_key5
    print('What do you want to decrypt?')
    text = input()
    how_long_text = int(len(text))
    space = ' '
    result_cesar = ''
    result_cesar_base64 = ''
    result_cesar_base64_2 = ''
    result = ""
    result2 = ''
    result_end = ''
    result2_end = ''
    result3 = ''
    result3_end = ''
    # Определение сложности шифрования
    # Шифр сложнее
    if text[0]==medium[0]:
        if text[1]==medium[1]:
            if text[2]==medium[2]:
                encription_dif = 'Hard and short encryption'
                # Расшифровка второго base64
                base64_message = text[3:]
                base64_bytes = base64_message.encode('ascii')
                message_bytes = base64.b64decode(base64_bytes)
                message = message_bytes.decode('ascii')
                message_split = message.split()
                # Расшифровка вторых win кодов
                how_many_codes = message.count(" ")
                where_codes = message.find(" ")
                for i in range(how_many_codes):
                    message_split_int = int(message_split[i])
                    message.find(" ")
                    b=str(message_split_int-crypt_key1-crypt_key2*crypt_key3)
                    result+=b+space
                    result_split = result.split()
                    result_fix = result_split[i]
                    result_preend = chr(int(result_fix))
                    result_end += result_preend
                # Расшифровка первого base64
                base64_message = result_end
                base64_bytes = base64_message.encode('ascii')
                message_bytes = base64.b64decode(base64_bytes)
                message = message_bytes.decode('ascii')
                message_split = message.split()
                # Расшифровка первых win кодов
                how_many_codes = message.count(" ")
                for i in range(how_many_codes):
                    message_split_int = int(message_split[i])
                    message.find(" ")
                    b=str(message_split_int-crypt_key1*crypt_key2-crypt_key3)
                    result2+=b+space
                    result_split = result2.split()
                    result_fix = result_split[i]
                    result_preend = chr(int(result_fix))
                    result2_end += result_preend
                print(result2_end)
                sys.exit()
    # Сложный шифр
    if text[0]==hard[0]:
        if text[1]==hard[1]:
            if text[2]==hard[2]:
                # Расшифровка третьего base64
                encription_dif = 'Very hard, but long encryption'
                base64_message = text[3:]
                base64_bytes = base64_message.encode('ascii')
                message_bytes = base64.b64decode(base64_bytes)
                message = message_bytes.decode('ascii')
                message_split = message.split()
                # Расшифровка третьих win кодов
                how_many_codes = message.count(" ")
                for i in range(how_many_codes):
                    message_split_int = int(message_split[i])
                    message.find(" ")
                    b=str(message_split_int-crypt_key4*4+crypt_key5*5)
                    result3+=b+space
                    result_split = result3.split()
                    result_fix = result_split[i]
                    result_preend = chr(int(result_fix))
                    result3_end += result_preend
                # Расшифровка второго base64
                base64_message = result3_end
                base64_bytes = base64_message.encode('ascii')
                message_bytes = base64.b64decode(base64_bytes)
                message = message_bytes.decode('ascii')
                message_split = message.split()
                # Расшифровка вторых win кодов
                how_many_codes = message.count(" ")
                where_codes = message.find(" ")
                for i in range(how_many_codes):
                    message_split_int = int(message_split[i])
                    message.find(" ")
                    b=str(message_split_int-crypt_key1-crypt_key2*crypt_key3)
                    result+=b+space
                    result_split = result.split()
                    result_fix = result_split[i]
                    result_preend = chr(int(result_fix))
                    result_end += result_preend
                # Расшифровка первого base64
                base64_message = result_end
                base64_bytes = base64_message.encode('ascii')
                message_bytes = base64.b64decode(base64_bytes)
                message = message_bytes.decode('ascii')
                message_split = message.split()
                # Расшифровка первых win кодов
                how_many_codes = message.count(" ")
                for i in range(how_many_codes):
                    message_split_int = int(message_split[i])
                    message.find(" ")
                    b=str(message_split_int-crypt_key1*crypt_key2-crypt_key3)
                    result2+=b+space
                    result_split = result2.split()
                    result_fix = result_split[i]
                    result_preend = chr(int(result_fix))
                    result2_end += result_preend
                print(result2_end)
                sys.exit()