import random
import enums
from math import pi
from py2neo import Graph, Node, NodeMatcher

def choose_default_value(attribute_name: str, graph):
    scope = None
    query = f"""
    MATCH (n:Attribute)
    WHERE n.name = "{attribute_name}"
    RETURN n
    LIMIT 1
    """
    result = graph.run(query).evaluate()
    if "range" in result.keys():
        # if str(result["range"]).startswith("["):
        #     lower_closed = True
        # else:
        #     lower_closed = False
        # if str(result["range"]).endswith("["):
        #     upper_closed = False
        # else:
        #     upper_closed = True
        temp = result["range"][1:len(result["range"]) - 1]
        lower_value = temp.split("..")[0]
        upper_value = temp.split("..")[1]
        contain_pi = False
        if upper_value == "inf":
            upper_value = 1000000
        elif upper_value == "2*PI":
            upper_value = 2.0
            contain_pi = True
        elif upper_value == "PI":
            upper_value = 1.0
            contain_pi = True
        elif "arclengt" in upper_value:
            upper_value = 30
        else:
            upper_value = float(upper_value)

        if lower_value == "-inf":
            lower_value = 1000000
        elif lower_value == "-2*PI":
            lower_value = 2.0
            contain_pi = True
        elif lower_value == "-PI":
            lower_value = 1.0
            contain_pi = True
        else:
            lower_value = float(lower_value)

        if contain_pi:
            return str(round(pi * random.uniform(lower_value, upper_value), 6))

        return str(round(random.uniform(lower_value, upper_value), 6))
    elif "unit" in result.keys():
        if result["unit"] == "rad":
            return str(round(pi * random.uniform(0, 0.5), 6))
        else:
            if result["type"] == "int":
                return str(round(random.randint(5, 10), 6))
            elif result["type"] == "double":
                return str(round(random.uniform(5, 10), 6))
    elif result["type"] in enums.ENUM_TYPES:
        return random.choice(enums.ENUM_TYPES[result["type"]])
    elif result['name'] == 'name':
        return "TESTNAME"
    elif result['name'] == 'filepath':
        return '/null'
    else:
        return str(round(random.uniform(0, 1), 6))


if __name__ == '__main__':
    uri = "bolt://localhost:7687"  # 替换为您的 Neo4j 服务器地址
    username = "neo4j"
    password = "12345678"
    graph = Graph(uri, auth=(username, password))
    matcher = NodeMatcher(graph)
    nodes = matcher.match("Attribute")
    for node in nodes:
        print(node)
        print(str(choose_default_value(node["colorType"], graph)))
