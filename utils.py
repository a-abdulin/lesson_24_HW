import re


# CMD_MAPPING = {
#     'filter': filter_,
#     'map': map_,
#     'unique': unique_,
#     'sort': sort_,
#     'limit': limit_,
# }



def filter_(param: str, data: list[str]) -> list[str]:
    return list(filter(lambda row: param in row, data))

def map_(param: str, data: list[str]) -> list[str]:
    col_num = int(param)
    return list(map(lambda row: row.split(' ')[col_num], data))

def unique_(param, data: list[str]) -> list[str]:
    result = []
    seen = set()
    for row in data:
        if row in seen:
            continue
        else:
            result.append(row)
            seen.add(row)
    return result

def sort_(param: str, data: list[str]) -> list[str]:
    if param == 'asc':
        order = True;
    else:
        order = False
    return sorted(data, reverse=order)

def limit_(param: str, data: list[str]) -> list[str]:
    num = int(param)
    return data[:num]


def regex_(param: str, data: list[str]) -> list[str]:
    if 'png' in param:
        regex_param = 'images\/\S*\.png'
    else:
        raise ValueError

    patern_ = re.compile(regex_param)
    result = []
    for line in data:
        item = patern_.findall(line)
        if item:
            result.append(line)
    return result

# images/*.png
# images\/\S*\.png

def get_query(cmd: str, param, data=None):
    if cmd == 'filter':
        return filter_(param=param, data=data)
    elif cmd == 'limit':
        return limit_(param=param, data=data)
    elif cmd == 'map':
        return map_(param=param, data=data)
    elif cmd == 'sort':
        return sort_(param=param, data=data)
    elif cmd == 'unique':
        return unique_(param=param, data=data)
    elif cmd == "regex":
        try:
            return regex_(param=param, data=data)
        except ValueError as e:
            print('Ошибка параметра regex')


    # return CMD_MAPPING[cmd](param=param, data=data)


# res = get_query('map', '0')
# res = get_query('limit', 5, res)
# print(res)

