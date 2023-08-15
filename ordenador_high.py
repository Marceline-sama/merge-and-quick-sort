import threading

class Sorter:
    def __init__(self):
        pass

    def particiona(self, valores, inicio, fim):
        pivo = valores[fim]
        i = inicio - 1 
        for j in range(inicio, fim):
            if valores[j] <= pivo:
                i += 1
                valores[i], valores[j] = valores[j], valores[i]  
        valores[i + 1], valores[fim] = valores[fim], valores[i + 1]
        return i + 1

    def quick_sort(self, valores, inicio, fim) -> [int]:
        return [1]

    def merge(self, esquerda, direita) -> [int]:

        merged = []
        i = j = 0
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                merged.append(esquerda[i])
                i += 1
            else:
                merged.append(direita[j])
                j += 1
        merged.extend(esquerda[i:])
        merged.extend(direita[j:])
        return merged        

    def merge_sort(self, valores) -> [int]:

        return [1]
