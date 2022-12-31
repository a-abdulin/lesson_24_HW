
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


FILE_NAME = './apache_logs.txt'

def read_file():
    with open(FILE_NAME) as file:
        file_data = list(map(lambda row: row.strip(), file))
    return file_data


def get_query(cmd: str, param, data=None):
    if not data:
        data = read_file()
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

    # return CMD_MAPPING[cmd](param=param, data=data)


# res = get_query('map', '0')
# res = get_query('limit', 5, res)
# print(res)

