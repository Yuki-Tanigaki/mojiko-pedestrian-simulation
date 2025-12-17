import random
import copy

population_size = 20  # 個体群サイズ
num_gene = 100       # 遺伝子長（ビットの数）
max_generations = 200 # 最大世代数
tournament_size = 20   # トーナメント選択で使う個体数
mutation_rate = 0.4   # 突然変異確率

class GA:
    def __init__(self, population_size, num_gene, generations, tournament_size, mutation_rate):
        # 引数をクラスの属性に保存
        self.population_size = population_size
        self.num_gene = num_gene
        self.generations = generations
        self.tournament_size = tournament_size
        self.mutation_rate = mutation_rate
        self.population = []  # 個体群を初期化

    def create_random_individual(self):
        # 個体をランダムに生成する（0または1のリスト）
        return [random.randint(0, 1) for _ in range(self.num_gene)]

    def initialize(self):
        # 初期個体群を生成する
        self.population = [self.create_random_individual() for _ in range(self.population_size)]

    def fitness(self, individual):
        def trap(u, k):
            if u == k:
                return k  # グローバル最適（すべて1）
            else:
                return k - 1 - u  # 局所最適（すべて0のとき最大）

        k = 5  # ブロックサイズ
        total = 0
        for i in range(0, len(individual), k):
            block = individual[i:i + k]
            u = sum(block)
            total += trap(u, k)
        return total

    def tournament_selection(self):
        # トーナメント選択を行い、良い個体を1つ返す
        candidates = random.sample(self.population, self.tournament_size)
        best = max(candidates, key=self.fitness)
        return copy.deepcopy(best)  # 元個体を壊さないようコピー

    def uniform_crossover(self, p1, p2):
        # 一様交叉（各遺伝子位置ごとにランダムにどちらかの親から選ぶ）
        return [p1[i] if random.random() < 0.5 else p2[i] for i in range(self.num_gene)]

    def bitflip_mutation(self, individual):
        # mutation_rate の確率で0/1を反転させる
        return [1 - gene if random.random() < self.mutation_rate else gene for gene in individual]

    def replacement(self, new_population):
        # populationをnew_populationに置き換える
        self.population = new_population

    def run(self):
        self.initialize()

        # 全体のベスト個体を記録（初期世代の中から）
        best_individual = max(self.population, key=self.fitness)
        best_fitness = self.fitness(best_individual)

        for generation in range(self.generations):
            new_population = []

            for _ in range(self.population_size):
                p1 = self.tournament_selection()
                p2 = self.tournament_selection()
                child = self.uniform_crossover(p1, p2)
                child = self.bitflip_mutation(child)
                new_population.append(child)

            self.replacement(new_population)

            # 現世代のベスト個体
            current_best = max(self.population, key=self.fitness)
            current_fitness = self.fitness(current_best)
            print(f"世代 {generation}: 適応度 = {current_fitness}")

            # 過去も含めたベスト個体の更新
            if current_fitness > best_fitness:
                best_individual = current_best
                best_fitness = current_fitness

        # 最終的なベスト個体の出力
        print(f"\n最良個体（全世代通算）: {best_individual}")
        print(f"適応度: {best_fitness}")


# 実行用コード
ga = GA(population_size, num_gene, max_generations, tournament_size, mutation_rate)
ga.run()
