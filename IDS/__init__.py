import json

wieght_k = 1
wieght_cost = 2
wieght_impact = 1

def load_json():
    with open('data.json') as file:
        return json.load(file)

def sort_alt(data, type, reverse=False): 
    return sorted(data['Alt'], key=lambda alternative: alternative[type], reverse=reverse)
 
def optimus(sort_cost, sort_impact, sort_k, max_points):
    result = [] 
    for index in range(max_points):
        result.append(0)
    
    index = max_points
    for value in sort_cost:
        id = value['id']
        result[id - 1] += index * wieght_cost
        index -= 1

    index = max_points
    for value in sort_impact:
        id = value['id']
        result[id - 1] += index * wieght_impact
        index -= 1

    index = max_points
    for value in sort_k:
        id = value['id']
        result[id - 1] += index * wieght_k
        index -= 1

    print(result)

data = load_json()
sort_cost = sort_alt(data, 'cost')
sort_impact = sort_alt(data, 'impact', True)
sort_k = sort_alt(data, 'k', True)

MAX_POINTS = len(data['Alt'])

optimus(sort_cost, sort_impact, sort_k, MAX_POINTS)