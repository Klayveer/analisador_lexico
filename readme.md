# Analisador Léxico para Linguagem C

## 📋 Descrição

Este projeto implementa um **Analisador Léxico (Lexer)** para a linguagem C, desenvolvido como parte da disciplina de Compiladores. O analisador é capaz de identificar tokens, classificá-los e construir uma tabela de símbolos para identificadores.

## 🎯 Funcionalidades

- **Análise Léxica Completa**: Reconhece tokens da linguagem C
- **Tabela de Símbolos**: Armazena identificadores com IDs únicos
- **Detecção de Erros**: Identifica caracteres inválidos
- **Suporte a Comentários**: Ignora comentários de linha (`//`) e bloco (`/* */`)
- **Pré-processamento**: Ignora diretivas de pré-processador (`#include`, `#define`, etc.)
- **Rastreamento de Linhas**: Mantém número de linha para cada token

## 🔧 Tipos de Tokens Reconhecidos

### Palavras-chave (Keywords)
```
int, void, if, else, while, return, for, switch, case, break, 
default, struct, typedef, float, char, const, sizeof, NULL, 
malloc, realloc, free, printf, scanf, strcmp, qsort, srand, time
```

### Operadores
- **Aritméticos**: `+`, `-`, `*`, `/`, `%`
- **Comparação**: `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Lógicos**: `&&`, `||`
- **Atribuição**: `=`
- **Incremento/Decremento**: `++`, `--`
- **Acesso a Membro**: `->`, `.`
- **Ternário**: `?`, `:`
- **Bitwise**: `&`, `|`, `^`, `~`

### Delimitadores
- Parênteses: `(`, `)`
- Chaves: `{`, `}`
- Colchetes: `[`, `]`
- Outros: `,`, `;`

### Literais
- **Números**: Inteiros e decimais (ex: `42`, `3.14`)
- **Strings**: Texto entre aspas duplas (ex: `"Hello"`)
- **Identificadores**: Nomes de variáveis, funções, etc.

## 🚀 Como Usar

### Requisitos
- Python 3.6 ou superior

### Execução do Analisador

1. **Análise de arquivo C**:
```bash
python analisador.py
```

2. Digite o nome do arquivo quando solicitado:
```
Digite o nome do arquivo .c para analisar: codigo_teste.c
```

3. O programa irá exibir:
   - Lista completa de tokens encontrados
   - Tabela de símbolos com identificadores e seus IDs

### Exemplo de Saída

```
Iniciando análise léxica...
==============================
Análise concluída com sucesso!
==============================

--- 1. LISTA DOS TOKENS ---
Tipo            | Valor                                    | Linha
------------------------------------------------------------
KEYWORD         | int                                      | 1    
IDENT           | #1                                       | 1    
LPAREN          | (                                        | 1    
RPAREN          | )                                        | 1    
LBRACE          | {                                        | 1    
KEYWORD         | return                                   | 2    
NUMBER          | 0                                        | 2    
OP_SEMICOLON    | ;                                        | 2    
RBRACE          | }                                        | 3    

--- 2. TABELA DE SÍMBOLOS (Identificadores) ---
Quantidade: 1
ID    | Símbolo            
------------------------------
#1    | main               
```

## 📁 Estrutura do Projeto

```
├── analisador.py      # Analisador léxico principal
├── codigo_teste.c     # Arquivo de teste 1
├── codigo_teste2.c    # Arquivo de teste 2
├── .gitignore         # Arquivos ignorados pelo Git
└── readme.md          # Este arquivo
```

## 🔍 Arquitetura do Analisador

### 1. Especificação de Tokens
Usa expressões regulares para definir padrões de tokens. A ordem é crucial - tokens mais específicos vêm primeiro.

### 2. Compilação de Regex
Combina todas as expressões regulares em um único pattern compilado para eficiência.

### 3. Processamento
- Itera pelo código fonte usando o regex compilado
- Identifica tipo e valor de cada token
- Rastreia números de linha (incluindo comentários multilinha)
- Constrói tabela de símbolos com IDs únicos
- Substitui identificadores por referências (#ID)

### 4. Tratamento de Erros
Caracteres não reconhecidos geram erro léxico e interrompem a análise.

## 📝 Exemplos de Código de Entrada

### Exemplo 1: Programa Simples
```c
int main() {
    int x = 10;
    return 0;
}
```

### Exemplo 2: Struct com Ponteiros
```c
typedef struct Node {
    int data;
    struct Node *next;
} Node;

void insert(Node **head, int value) {
    Node *newNode = malloc(sizeof(Node));
    newNode->data = value;
}
```

### Exemplo 3: Operadores e Controle de Fluxo
```c
int main() {
    int x = 5;
    if (x > 0 && x < 10) {
        x++;
    }
    int result = (x == 5) ? 1 : 0;
    return result;
}
```

## ⚠️ Limitações Conhecidas

- Não valida a sintaxe da linguagem C (apenas léxica)
- Não reconhece alguns tokens avançados (macros complexas, literais hexadecimais)
- Strings não suportam caracteres de escape
- Comentários devem estar bem formados (sem EOF em comentário de bloco aberto)

## 🛠️ Possíveis Melhorias Futuras

- [ ] Suporte a literais hexadecimais e octais
- [ ] Reconhecimento de caracteres de escape em strings
- [ ] Melhor tratamento de erros com sugestões
- [ ] Análise sintática (parser)
- [ ] Geração de árvore sintática abstrata (AST)
- [ ] Modo interativo (REPL)
- [ ] Exportação de tokens para JSON/XML

## 👨‍💻 Autor

Desenvolvido como projeto acadêmico para a disciplina de Compiladores.

## 📄 Licença

Este projeto é de uso educacional.

---

**Nota**: Para dúvidas ou sugestões, consulte a documentação do código em `analisador.py`.
