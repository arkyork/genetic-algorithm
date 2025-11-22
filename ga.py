from dataclasses import dataclass,field
import random

@dataclass
class GA:
    
    # 長さ
    gene_length: int = 10
    
    # 集団のサイズ
    size: int = 10
    generations: int = 2
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
        new_gene = ""
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
    # 選択
    def selection(self):
        a,b = random.sample(self.population,2)
        # トーナメント方式
        return a if self.fitness(a) > self.fitness(b) else b

    # アルゴリズムの実行
    def run(self):
        for generation in range(self.generations):
            
            # エリート個体の保存
            elite = max(self.population, key=self.fitness)

            new_population = []

            while len(new_population) < self.size:
                parent1 = self.selection()
                parent2 = self.selection()
                child1, child2 = self.cross_over(parent1, parent2)
                new_population.append(self.mutate(child1))
                if len(new_population) < self.size:
                    new_population.append(self.mutate(child2))
            


            # 最良個体を置き換え
            new_population[random.randrange(self.size)] = elite
            self.population = new_population

            # 現世代の最適解
            best = max(self.population, key=self.fitness)
            print(f"Generation {generation+1}: Best = {best} → {self.fitness(best)}")
    
        
        return max(self.population, key=self.fitness)