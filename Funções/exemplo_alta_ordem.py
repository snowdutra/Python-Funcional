from exemplo_primeira_classe import dobro, quadrado


def processar(titulo = 'Dobro', lista = [2,6] , funcao = quadrado):
    print(f'Procesando: {titulo}')
    for i in lista:
        print(i, ' => ', funcao(i))




if __name__  == '__main__':
    processar('Dobro', [2,6,3,9], dobro)
    processar('Quadrado', [2,6,3,9], quadrado)
    fun = quadrado
    processar('Quadrado', [2,6,3,9], fun)
    processar()
