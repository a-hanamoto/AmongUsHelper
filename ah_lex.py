import ply.lex as lex

tokens = (
    "MEMBER",
    "NONE",
    "NUMBER",
    "COMMA",
    "SEMI",
    "TRUST",
    "DOUBT",
    "DEAD",
    "EJECT",
    "SKIP",
)

t_MEMBER = r"(?!trust|doubt|dead|eject|skip|none)[A-Za-z]+"
t_NONE = r"none"
t_NUMBER = r"[0-9]+"
t_COMMA = r","
t_SEMI = r";"
t_TRUST = r"trust"
t_DOUBT = r"doubt"
t_DEAD = r"dead"
t_EJECT = r"eject"
t_SKIP = r"skip"
t_ignore = " \t\n"
t_ignore_COMMENT = r"\#.*"


def t_error(t):
    print(f"lex error: {t.value[0]}")
    t.lexer.skip(1)


lexer = lex.lex()


def lex_test():
    with open("./data.txt") as f:
        data = f.read()
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)


if __name__ == "__main__":
    lex_test()
