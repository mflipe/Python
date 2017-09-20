# Imports
import random, re

# Funções:

# GUI
def banner(words, lines, size):
    print(''.center(size, lines))
    print(words.center(size))
    print(''.center(size, lines))

def forca(n):
    v = ['      ┌────┐      \n'
         '      │    │      \n'
         '      │    ☻      \n'
         '      │   /|\\    \n'
         '      │   / \\    \n'
         '      │           \n'
         '    ──┴── ',
         '      ┌────┐      \n'
         '      │    │      \n'
         '      │    ☻      \n'
         '      │   /|\\    \n'
         '      │   /       \n'
         '      │           \n'
         '    ──┴── ',
         '      ┌────┐      \n'
         '      │    │      \n'
         '      │    ☻      \n'
         '      │   /|\\    \n'
         '      │           \n'
         '      │           \n'
         '    ──┴── ',
         '      ┌────┐      \n'
         '      │    │      \n'
         '      │    ☻      \n'
         '      │   /|      \n'
         '      │           \n'
         '      │           \n'
         '    ──┴── ',
         '      ┌────┐      \n'
         '      │    │      \n'
         '      │    ☻      \n'
         '      │    |      \n'
         '      │           \n'
         '      │           \n'
         '    ──┴── ',
         '      ┌────┐      \n'
         '      │    │      \n'
         '      │    ☻      \n'
         '      │           \n'
         '      │           \n'
         '      │           \n'
         '    ──┴── ',
         '      ┌────┐      \n'
         '      │    │      \n'
         '      │           \n'
         '      │           \n'
         '      │           \n'
         '      │           \n'
         '    ──┴── ',
         ]
    return v[n]

# Engine
def swithDificuldade(x):
    return {
        'fácil': 1, 'facil': 1, 1: 1,
        'normal': 2, 2:2,
        'difícil': 3, 'dificil': 3, 3:3,
        'frutas': 4, 4:4
    }[x]

def dificult():
    nivel = 0
    print('Escolha a dificuldade que pretende jogar: ')
    banner('''Fácil: nivel mais básico, recomendado para jogadores iniciantes.
Normal: nivel normal de jogo, recomendado para jogadores casuais que buscam diversão.
Difícil: nivel mais desafiador, recomendado para jogadores que gostam de desafios.''', '—', 60)
    while nivel == 0:
        dificuldade = input('Qual dificuldade pretende jogar? \n')
        try:
            nivel = swithDificuldade(dificuldade.lower())
        except KeyError:
            nivel = 0
            print('Dificuldade não reconhecida, tente novamente.')
        # TODO: Refatorar
        if nivel == 1:
            x = input('Será iniciada uma seção na dificuldade FÁCIL. Deseja prosseguir? \n')
            if x.lower() == 'sim':
                print('Processeguindo.')
                break
            else:
                print('Retornando.')
                nivel = 0
        elif nivel == 2:
            x = input('Será iniciada uma seção na dificuldade NORMAL. Deseja prosseguir? \n')
            if x.lower() == 'sim':
                print('Processeguindo.')
                break
            else:
                print('Retornando.')
                nivel = 0
        elif nivel == 3:
            x = input('Será iniciada uma seção na dificuldade DIFÍCIL. Deseja prosseguir? \n')
            if x.lower() == 'sim':
                print('Processeguindo.')
                break
            else:
                print('Retornando.')
                nivel = 0
    return nivel

def selecionaPalavra(lst, lvl):
    random.shuffle(lst[lvl - 1])
    return random.choice(dificuldades[n - 1])

def mascara(palavra):
    # print("Mascara: ")
    regex = re.compile(r'.{1}')
    # print(palavra) # Debug
    rString = regex.sub(r'_ ', palavra)
    # print(rString) # Debug
    return rString

def tentativa(tentadas, palavra, palavraEscondida):
    acertos = 0
    palavra = palavra.upper()
    # Checa se a letra já foi tentada
    t=0
    while t==0:
        letra = input('Chute uma letra: ')
        letra = letra.upper()
        if len(letra) != 1 or type(letra) != str:
            print("Esta letra não é válida. Tente novamente.")
            t = 0
        else:
            t = 1
        for letter in tentadas:
            if letra == letter:
                print("Esta letra já foi tentada. Tente novamente.")
                t = 0
            else:
                t = 1

    tentadas.append(letra)
    tentadas.sort()
    aux = ''
    for i in range(len(palavra)):
        if letra == palavra[i]:
            # print("Desmascara: ")    # Debug
            # print(palavraEscondida)  # Debug
            aux = list(palavraEscondida)
            aux[i*2] = palavra[i]
            palavraEscondida = ''.join(aux)
            # print(palavraEscondida)  # Debug
            acertos += 1

    if len(aux) > 0:
        acertou = True
    else:
        acertou = False

    return tentadas, palavraEscondida, acertou, acertos

# Main
# Lista de palavras classificadas por dificuldade/assunto.
tentadas = []
facil = ['Pinguin']
normal = ['normal1', 'normal2', 'normal3']
dificil = ['dificil1', 'dificil2', 'dificil3']
frutas = [  'Abacate', 'Abacaxi', 'Abiu', 'Abrico', 'Açai', 'Acerola', 'Akee', 'Ameixa', 'Amendoa', 'Amora',
            'Anonaceas', 'Araça', 'Atemoya', 'Avela',
            'Babaco', 'Bacaba', 'Bacuri', 'Banana', 'Baru', 'Buriti', 'Bilimbi', 'Biribá', 'Butiá',
            'Cabeludinha', 'Cacau', 'Cagaita', 'Cajá manga', 'Cereja', 'Caimito', 'Caja', 'Conde', 'Cupuaçu', 'Caju',
            'Calabaça', 'Carambola', 'Calabura', 'Coco', 'Calamondin', 'Cambuca', 'Cagaita', 'Cambuci',
            'Damasco', 'Dovyalis', 'Duriao',
            'Embauba',
            'Feijoa', 'Figo', 'Framboesa', 'Fruta Pão', 'Frutas do Cerrado',
            'Glicosmis', 'Goiaba', 'Granadilla', 'Graviola', 'Groselha', 'Grumixama', 'Guabiju', 'Guabiroba', 'Guarana',
            'Guariroba',
            'Heisteria', 'Himbeere',
            'Ilama', 'Inga',
            'Jabuticaba', 'Jaca', 'Jambo', 'Jambolao', 'Jaracatia', 'Jamelao', 'Jatoba', 'Jenipapo', 'Jeriva', 'Jeriba',
            'Jujuba',
            'Kiwi',
            'Langsat', 'Laranja', 'Lichia', 'Limao', 'Limas Ácidas', 'Limas Doces', 'Longan', 'Lucuma',
            'Mabolo', 'Maça', 'Macadamia', 'Mamao', 'Mamey', 'Mamoncillo', 'Mana Cubiu', 'Manga', 'Mangaba', 'Mangostão',
            'Maracujá', 'Morango', 'Marmeladinha', 'Marmelo', 'Marolo', 'Marula', 'Massala', 'Melancia', 'Melao',
            'Melao de Sao Caetano', 'Mirtilo', 'Morango', 'Murici',
            'Naranjilla', 'Nectarina', 'Nespera', 'Noni', 'Noz Peca',
            'Olho De Boi',
            'Pequi', 'Pera', 'Pessego', 'Physalis', 'Pinha', 'Pinhao', 'Pistache', 'Pitanga', 'Pitangão', 'Pitaya',
            'Pitomba', 'Pulasan', 'Pupunha',
            'Quina',
            'Rambutão', 'Roma',
            'Salak', 'Santol', 'Sapoti', 'Sapucaia', 'Sapucaia', 'Seriguela',
            'Taiuva', 'Tamara', 'Tamarindo', 'Tangerina', 'Taruma', 'Tomate Arboreo', 'Toranja',
            'Umbu', 'Ume', 'Uva', 'Uvaia',
            'Veludo',
            'Wampi',
            'Xixa',
            'Yamamomo',
            'Zimbro', 'Zitrone',
]

dificuldades = [facil, normal, dificil, frutas]

# Introdução/ TODO: Menu
C = 100
banner('Jogo da forca', '=', C)

# TODO: Seleção de dificuldade/assunto
n = dificult() # 0 = Falha, 1 = Fácil, 2 = Normal, 3 = Difícil, ...

banner('*  Inicio do jogo  *', '*', C)
palavra = selecionaPalavra(dificuldades, n)
palavraEscondida = mascara(palavra)

tentativas = 6
pontos = 1

while tentativas > 0:
    print(forca(tentativas), palavraEscondida)
    print("Número de Tentativas: ", tentativas)
    print("Letras Tentadas: ", tentadas)

    # TODO: Pedir uma
    acertos = 0
    tentadas, palavraEscondida, acertou, acertos = tentativa(tentadas, palavra, palavraEscondida)

    # TODO: Pontuar ou retirar vida/tentativa
    if acertou:
        print("Parabéns, você acertou {} letra(s). ".format(acertos))
        pontos += acertos
        if pontos == len(palavra)+1:

            tentativas = 0
    else:
        tentativas -= 1

if pontos == len(palavra)+1:
    print(forca(tentativas), palavraEscondida)
    print("Número de Tentativas: ", tentativas)
    print("Letras Tentadas: ", tentadas)
    print("Parabéns, você venceu!")
else:
    print(forca(0))
    print("Que pena, suas tentativas acabaram")
    print("A palavra era: ", palavra.upper())