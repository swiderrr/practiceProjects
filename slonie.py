#Jak powinno wyglądać wejście i pobieranie danych. Nie rozumiem z treści maila?
#Czy robić sprawdzanie granic zmiennych (np. try, except)?
#Czy zamknąć to w klasie?
#Czy powinienem wrzucić tutaj dowód poprawności rozwiązania
'''
n = 6
weights = [2400, 2000, 1200, 2400, 1600, 4000]
oriPosition = [1, 4, 5, 3, 6, 2]
movedPosition = [5, 3, 2, 4, 6, 1]
'''


n = 8
weights = [197, 170, 124, 180, 128, 163, 188, 140]
oriPosition = [2, 5, 7, 8, 1, 3, 6, 4]
movedPosition = [5, 6, 1, 8, 2, 4, 7, 3]

def simple_cycles(original, moved):

    #Należy dodać ograniczenia ograniczenia zbiorów dla n i m
    visited = [False for i in range(n)]
    c = 0
    cycle = {}
    for i in range(n):
        cycle[i] = []
        if not visited[i]:
            c =+ 1
            x = i
            while not visited[x]:
                visited[x] = True
                cycle[i].append(original[x])
                x = moved.index(original[x])

    return cycle

#Wyznaczanie parametrów cykli
def cycle_parameters(cyclesList):
    w = 0
    for i in range(len(cyclesList)):
        cycleSum = 0
        cycleMinimum, globalMinimum = 6500, min(weights)
        if len(cyclesList[i]) > 1:
            for e in cyclesList[i]:
                elephantWeight = weights[e-1]
                cycleSum = cycleSum + elephantWeight
                cycleMinimum = min(cycleMinimum, elephantWeight)

            globalMinimum = min(globalMinimum, cycleMinimum)
            methodOne = cycleSum + (len(cyclesList[i]) - 2) * cycleMinimum
            methodTwo = cycleSum + cycleMinimum + (len(cyclesList[i]) + 1) * globalMinimum

            w = w + min(methodOne, methodTwo)

    return w


print(cycle_parameters(simple_cycles(oriPosition, movedPosition)))