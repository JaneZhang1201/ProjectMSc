import csv
import random

concepts = ['concept1', 'concept2', 'concept3', 'concept4', 'concept5']
num_pairs = len(concepts) * (len(concepts) - 1) // 2  # 计算总共的配对数量

with open('concept_pairs.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Index', 'Concept1', 'Concept2', 'Value'])  # 写入CSV文件的表头

    pair_count = 0
    for i in range(len(concepts)):
        for j in range(i + 1, len(concepts)):
            pair_count += 1
            value = random.uniform(-1, 1)  # 生成介于-1和1之间的随机数值
            writer.writerow([pair_count, concepts[i], concepts[j], value])
