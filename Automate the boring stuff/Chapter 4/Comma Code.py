# Comma Code

# Say you have a list value like this:
# spam = ['apples', 'bananas', 'tofu', 'cats']

# Write a function that takes a list value as an argument and
# returns a string with all the items separated by a comma and a space,
# with and inserted before the last item. For example,
# passing the previous spam list to the function would return
# 'apples, bananas, tofu, and cats'.
# But your function should be able to work with any list value passed to it.

def funcLista(lista):
    saida = ""
    for index in range(len(lista)-1):
        saida += lista[index] + ", "
    saida += "and " + lista[len(lista)-1]
    print(saida)

# Main
lista = ['apples', 'bananas', 'tofu', 'cats']
funcLista(lista)