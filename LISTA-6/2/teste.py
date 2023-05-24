from assinaturaSimples import AssinaturaSimples
from assinaturaPremium import AssinaturaPremium

assinaturaSimples = AssinaturaSimples('Simples')
assinaturaPremium = AssinaturaPremium('Premium')

assinaturas = []

assinaturas.extend([assinaturaSimples, assinaturaPremium])

for i in assinaturas:
    print("Tipo de assinatura:", i._tipo)
    print("Preço da assinatura:", i.calcular_preco())
    print("Detalhes da assinatura:", i.exibir_detalhes())
    print()