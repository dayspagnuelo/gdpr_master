import itertools
import csv
import pandas

original_annotations = pandas.read_csv("tags.csv")
print(original_annotations)

deliberations = original_annotations['URI'].unique()
gephi_data = []

for deliberation in deliberations:
    tags = original_annotations[original_annotations['URI'] == deliberation]['Tag']
    combinations = list(itertools.combinations(tags, 2))
    for pairs in combinations:
        gephi_data.append([pairs[0], pairs[1], deliberation])

print(gephi_data)

fields = ['Source', 'Target', 'Page']

with open('data2.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(gephi_data)