from dataclasses import dataclass,field
import random

@dataclass
class GA:
    
    
    # 長さ
    gene_length: int = 5
    
    # 集団のサイズ
    size: int = 10
    generations: int = 30
    population: list[str] = field(init=False)

    # 突然変異や交叉
    cross_over_rate: float = 0.9
    mutation_rate: float = 0.1

    def __post_init__(self):
        # クラス作成後 population を初期化
        self.population = [self._random_gene() for _ in range(self.size)]

    def _random_gene(self) -> str:
        # ランダムなビット列を生成
        return ''.join(random.choice("01") for _ in range(self.gene_length))

    # 交叉
    def cross_over(self ,par1: str ,par2: str):
        if random.random() > self.cross_over_rate:
            return par1,par2

        random_point = random.randint(1,self.gene_length-1)
        # 子供の作成
        child1 = par1[:random_point] + par2[random_point:]
        child2 = par2[:random_point] + par1[random_point:]
        
        return child1, child2
    
    # 突然変異
    def mutate(self,gene: str) -> str:
        for bit in gene:
            if random.random() < self.mutation_rate:
                new_gene += "1" if bit == "0" else "0"
            else:
                new_gene += bit
        return new_gene
    
    # 適合度
    def fitness(self, gene:str) -> int:
        x = int(gene, 2)  # 2進 → 10進
        return x ** 2
    
    