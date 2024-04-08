from personagem import *
Astolfo = guerreiro(20,10,"Um cavaleiro com historico de insonia, panico e ataques de raiva",5)
#Imprime todos parametros do Astolfo
print(f"\nPERSONAGEM:\n{vars(Astolfo)}")
#Teste funcao usando parametro ataque
Astolfo.corte_rapido()