from lark import Lark, InlineTransformer
parser = Lark('''?sum: product
                     | sum "+" product   -> add
                     | sum "-" product   -> sub

                 ?product: item
                     | product "*" item  -> mul
                     | product "/" item  -> div

                 ?item: NUMBER           -> number
                      | "-" item         -> neg
                      | "(" sum ")"

                 %import common.NUMBER
                 %import common.WS
                 %ignore WS
         ''', start='sum')

class CalculateTree(InlineTransformer):
    from operator import add, sub, mul, truediv as div, neg
    number = float

def calc(expr):
    return CalculateTree().transform( parser.parse(expr) )

if __name__ == '__main__':
    print(calc("204 * 97"))