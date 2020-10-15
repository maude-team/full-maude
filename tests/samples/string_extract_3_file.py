import re


def select_text(arg):
    p = re.compile("\"([^\"]*)\"")
    f = open(arg)
    read_data = f.read()
    # print(read_data)
    result = p.search(read_data)
    f.close()
    if result:
        return result.group(1)  # [0:-1]
    else:
        # return "not found"
        raise Exception("not found")


# print(select_text('file.txt'))
