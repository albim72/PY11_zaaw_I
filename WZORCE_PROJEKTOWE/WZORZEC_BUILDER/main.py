from director import Director
from concretebuilder1 import ConcreteBuilder1

director = Director()
builder = ConcreteBuilder1()

director.builder = builder

print(f"\nProdukt minimalny")
director.build_minial_version()
builder.product.list_parts()

print(f"\nProdukt kompletny")
director.build_full_version()
builder.product.list_parts()

#moja wersja produkt AC
print("\nmoja wersja produktu AC:")
builder.produce_part_a()
builder.produce_part_c()
builder.product.list_parts()
