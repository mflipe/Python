# Strong Password Detection
# Write a function that uses regular expressions to make sure the password string it is passed is strong.
# A strong password is defined as one that is at least eight characters long, contains both uppercase
# and lowercase characters, and has at least one digit.
# You may need to test the string against multiple regex patterns to validate its strength.
import re

def f(x):
    return {
        1: "||||            ",
        2: "||||||||        ",
        3: "||||||||||||    ",
        4: "||||||||||||||||",
    }[x]

def pwStr(pw):
    pwStr = 0
    # Pelo menos 8 caracteres
    if len(pw) >= 8:
        pwStr += 1
    else:
        print('Fragilidade de Senha: Senha muito curta.')
    # Pelo menos 1 letra maiuscula
    maisculaRegex = re.compile(r'''
        [A-Z]
        ''', re.VERBOSE)
    if maisculaRegex.search(pw) == None:
        print('Fragilidade de Senha: Não possui nenhum caractere maiúsculo.')
    else:
        pwStr += 1
    # Pelo menos 1 letra minuscula
    minusculoRegex = re.compile(r'''
        [a-z]
        ''', re.VERBOSE)
    if minusculoRegex.search(pw) == None:
        print('Fragilidade de Senha: Não possui nenhum caractere minúsculo.')
    else:
        pwStr += 1
    # Pelo menos 1 número
    numeroRegex = re.compile(r'''
        [0-9]
        ''', re.VERBOSE)
    if numeroRegex.search(pw) == None:
        print('Fragilidade de Senha: Não possui nenhum caractere numérico.')
    else:
        pwStr += 1
    # Resultado
    print("Resultado".center(18, '='))
    print("[", f(pwStr), "]", sep="")
    print("".center(18, '='))

# Main
pwStr("isabeleisA1")