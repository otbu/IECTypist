
def main(text):

    from arpeggio import Optional, ZeroOrMore, OneOrMore, EOF
    from arpeggio import RegExMatch as _

    def number():     return _(r'\d*\.\d*|\d+')
    def factor():     return Optional(["+","-"]), [number, ("(", expression, ")")]
    def term():       return factor, ZeroOrMore(["*","/"], factor)
    def expression(): return term, ZeroOrMore(["+", "-"], term)
    def calc():       return OneOrMore(expression), EOF

    from arpeggio import ParserPython
    parser = ParserPython(calc)  # calc is the root rule of your grammar
    # Use param debug=True for verbose debugging
    # messages and grammar and parse tree visualization
    # using graphviz and dot

    parse_tree = parser.parse(text)
    pass

if __name__ == '__main__':
    main('-(4-1)*5+(2+4.67)+5.89/(.2+7)')