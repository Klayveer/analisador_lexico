import re  # regular expressions
import sys

def analisador_lexico_c(codigo_c):
    
    # 1. ESPECIFICAÇÃO DOS TOKENS USANDO EXPRESSÕES REGULARES
    # A ORDEM É CRUCIAL! Tokens mais específicos devem vir antes.
    especificacao_tokens = [
        # --- Regras para Ignorar ---
        
        ('COMMENT_BLOCK', r'/\*(.|\n)*?\*/'), 
        ('COMMENT_LINE',  r'//.*'),      
        ('PREPROC',   r'#.*'),           
        ('NEWLINE',   r'\n'),           
        ('SKIP',      r'[ \t]+'),        
        
        # --- Tokens da Linguagem ---
        
        ('KEYWORD',   r'\b(int|void|if|else|while|return|for|switch|case|break|default|struct|typedef|float|char|const|sizeof|NULL|malloc|realloc|free|printf|scanf|strcmp|qsort|srand|time)\b'),
        ('NUMBER',    r'\d+(\.\d+)?'),   
        ('IDENT',     r'[A-Za-z_][A-Za-z0-9_]*'),    
        ('STRING',    r'"[^"]*"'),        
        
        # --- Operadores ---
        
        ('OP_ARROW',  r'->'),            
        ('OP_COMP',   r'==|!=|<=|>=|<|>'), 
        ('OP_LOGIC',  r'&&|\|\|'),        
        ('OP_INCDEC', r'\+\+|--'),        
        ('OP_ASSIGN', r'='),            
        ('OP_ARITH',  r'[+\-*/%]'),        
        ('OP_COLON',  r':'),            
        ('OP_SEMICOLON', r';'),          
        ('OP_MEMBER', r'\.'),            
        ('OP_BITWISE',r'[&|^~]'),        
        ('OP_TERNARY', r'\?'),           
        
        # --- Delimitadores ---
        ('LPAREN',    r'\('),           
        ('RPAREN',    r'\)'),           
        ('LBRACE',    r'\{'),           
        ('RBRACE',    r'\}'),           
        ('COMMA',     r','),            
        ('LBRACKET',  r'\['),           
        ('RBRACKET',  r'\]'),           
        
        # --- Regra de Erro ---
        ('MISMATCH',  r'.'),            
    ]

    # 2. COMPILAÇÃO DO REGEX
    
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in especificacao_tokens)
    get_token = re.compile(tok_regex).finditer 

    # Estruturas para armazenar resultados
    lista_tokens = []
    tabela_simbolos = {}  
    id_counter = 1  
    
    # 3. PROCESSAMENTO DO CÓDIGO (Linha por Linha)
    line_num = 1
    
    print("Iniciando análise léxica...")
    print("="*30)

    for mo in get_token(codigo_c):
        kind = mo.lastgroup    
        value = mo.group()     

        if kind == 'NEWLINE':
            line_num += 1
        elif kind == 'COMMENT_BLOCK':
            line_num += value.count('\n')
        elif kind in ('SKIP', 'PREPROC', 'COMMENT_LINE'):
            pass
        elif kind == 'MISMATCH':
            print(f"*** ERRO LÉXICO ***: Caractere inesperado '{value}' na linha {line_num}")
            return None, None 
        else:
            token = (kind, value, line_num)
            lista_tokens.append(token)
            
            if kind == 'IDENT' and value not in tabela_simbolos:
                tabela_simbolos[value] = id_counter
                id_counter += 1

    # Substitui os identificadores na lista de tokens
    lista_tokens_com_ids = []
    for tipo, valor, linha in lista_tokens:
        if tipo == 'IDENT':
            id_value = tabela_simbolos[valor]
            lista_tokens_com_ids.append(('IDENT', f'#{id_value}', linha))
        else:
            lista_tokens_com_ids.append((tipo, valor, linha))
    
    print("Análise concluída com sucesso!")
    print("="*30)
    
    return lista_tokens_com_ids, tabela_simbolos

if __name__ == "__main__":
    
    nome_arquivo = input("Digite o nome do arquivo .c para analisar: ")

    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            codigo_para_analisar = f.read()
    except FileNotFoundError:
        print(f"*** ERRO: Arquivo '{nome_arquivo}' não encontrado. ***")
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"*** ERRO: O arquivo '{nome_arquivo}' não parece estar em UTF-8. ***")
        sys.exit(1)
        
    tokens, simbolos = analisador_lexico_c(codigo_para_analisar)

    if tokens is not None:
        
        # SAÍDA 1: LISTA DOS TOKENS
        print("\n--- 1. LISTA DOS TOKENS ---")
        print(f"{'Tipo':<15} | {'Valor':<40} | {'Linha':<5}")
        print("-"*60)
        for tipo, valor, linha in tokens:
            print(f"{tipo:<15} | {valor:<40} | {linha:<5}")

        # SAÍDA 2: TABELA DE SÍMBOLOS
        print("\n--- 2. TABELA DE SÍMBOLOS (Identificadores) ---")
        print(f"Quantidade: {len(simbolos)}")
        
        if len(simbolos) > 0:
            print(f"{'ID':<5} | {'Símbolo':<20}")
            print("-"*30)
            for simbolo, id_num in simbolos.items():
                print(f"#{id_num:<4} | {simbolo:<20}")