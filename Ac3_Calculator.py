import abc
from unittest import TestCase, main


class Calculadora(object):

    def calcular(self, value1, value2, operator):
        operacaoFabrica = OperacaoFabrica()
        operacao = operacaoFabrica.criar(operator)
        if (operacao == None):
            return 0
        else:
            resultado = operacao.executar(value1, value2)
            return resultado


class OperacaoFabrica(object):

    def criar(self, operator): 
        if (operator == 'soma'):
            return Soma()
        elif (operator == 'subtracao'):
            return Subtracao()
        elif (operator == 'divisao'):
            return Divisao()
        elif (operator == 'multiplicacao'):
            return Multiplicacao()


class Operacao(metaclass = abc.ABCMeta):

    @abc.abstractmethod
    def executar(self, value1, value2):
        pass


class Soma(Operacao):
    def executar(self, value1, value2):
        resultado = value1 + value2
        return resultado


class Subtracao(Operacao):
    def executar(self, value1, value2):
        resultado = value1 - value2
        return resultado


class Multiplicacao(Operacao):
    def executar(self, value1, value2):
        resultado = value1 * value2
        return resultado


class Divisao(Operacao):
    def executar(self, value1, value2):
        resultado = value1 / value2
        return resultado


class Testes(TestCase):

    def test_soma(self):
        calculator = Calculadora()
        result = calculator.calcular(50, 20, 'soma')
        print(result)
        self.assertEqual(result, 70)


    def test_multiplicacao(self):
        calculator1 = Calculadora()
        result = calculator1.calcular(20, 20, 'multiplicacao') 
        print(result)
        self.assertEqual(calculator1.calcular(20, 20, 'multiplicacao'), 400)

    
    def test_divisao(self):
        calculator2 = Calculadora()
        result = calculator2.calcular(500, 20, 'divisao')
        print(result)
        self.assertEqual(calculator2.calcular(1000, 20, 'divisao'), 50)
        

    def test_subtracao(self):
        calculator3 = Calculadora()
        result = calculator3.calcular(20, 100, 'subtracao')
        print(result)
        self.assertEqual(calculator3.calcular(20, 100, 'subtracao'), -80)
        

calculator = Calculadora()
z = calculator.calcular(50, 50, 'multiplicacao')
print(z)


if __name__ == '__main__':
    main()