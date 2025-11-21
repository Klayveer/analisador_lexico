/* TESTE DE ESTRESSE
   Objetivo: Quebrar o analisador
*/
int main(){
    // 1. Teste de "Colagem" (sem espacos)
    int a=10;if(a>=10){return 0;}

    // 2. Teste de Ambiguidade (Keywords vs IDs)
    int intervalo = 50;  // contem 'int'
    void avoid = 0;      // contem 'void'
    
    // 3. Numeros e Operadores Compostos
    float preco=12.99; 
    if(preco==12.99 && preco!=0) { preco++; }

    // 4. Armadilhas (Strings e Comentários)
    char* texto = "int x = 0; // isso nao eh comentario";
    // int b = 20; isso deve ser ignorado
    
    int _variavel_123 = 99; // ID com numero e underscore
}