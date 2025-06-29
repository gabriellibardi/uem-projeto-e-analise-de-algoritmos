from dataclasses import dataclass

@dataclass
class Tarefa:
    lucro: int
    prazo: int

def escolhe_tarefas(lista: list[Tarefa], num_tarefas: int, hora_limite: int):
    
    lista.sort(key=lambda t: t.prazo, reverse=True)

    while hora_limite > 0 and num_tarefas > 0:

        tarefas_disponiveis = []
        j = 0
        while j < num_tarefas and lista[j].prazo >= hora_limite:
            tarefas_disponiveis.append(lista[j])
            j += 1
        
        if tarefas_disponiveis != []:
            melhor_tarefa = max(tarefas_disponiveis, key=lambda t: t.lucro)
            lista.remove(melhor_tarefa)
            num_tarefas -= 1

        hora_limite -= 1

    return sum([tarefa.lucro for tarefa in lista])


def main():

    while True:
    
        try:
    
            input0 = input()
            n, h = input0.split()
            n, h = int(n), int(h)
        except:
    
            break
        lista_tarefas = []
        for _ in range(n):
    
            lucro, prazo = input().split()
            lucro, prazo = int(lucro), int(prazo)
            lista_tarefas.append(Tarefa(lucro, prazo))
        print(escolhe_tarefas(lista_tarefas, n, h))

        
if __name__ == "__main__":
    
    main()
