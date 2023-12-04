import xmlparser
from py2neo import Graph
from default_value_selector import choose_default_value
from validate import validate_file
import random

@DeprecationWarning
def find_key_in_nested_dict(dictionary, key_to_find):
    """
    递归查找嵌套字典中的 key
    dictionary: 嵌套字典
    key_to_find: 要查找的 key
    如果找到，返回对应的值；否则返回 None
    """
    if key_to_find in dictionary:
        return dictionary

    for key, value in dictionary.items():
        if isinstance(value, dict):
            # 如果当前值是字典，递归查找
            nested_result = find_key_in_nested_dict(value, key_to_find)
            if nested_result is not None:
                return nested_result
    # 如果所有分支都没有找到 key，返回 None
    return None

@DeprecationWarning
def mutate(file_path: str, result_path: str, attribute: str, graph, value=None):
    '''
    file_path: 待变异原文件路径
    result_path: 变异后新文件路径
    attribute: 待变异的属性名称
    graph: 数据库图
    value: 指定变异属性的变异值，默认为None，为None时表示随机变异
    '''
    data = xmlparser.xml2dict(file_path)
    attribute_to_mutate = find_key_in_nested_dict(data, '@'+attribute)
    if attribute_to_mutate is None:
        raise KeyError(f'Cannot find attribute:{attribute} in data')
    if value is not None:
        attribute_to_mutate['@'+attribute] = value
    else:
        attribute_to_mutate['@'+attribute] = choose_default_value(attribute, graph)
    xmlparser.dict2xml(data, result_path)
    validate_file(result_path)

def mutate_vehicle(catalog_location_path: str, graph):
    """
    变异Catalog中的Vehicle
    """
    def mutate(mutate_vehicle: dict):
        mutate_vehicle['@mass'] = choose_default_value('mass', graph)
        mutate_vehicle['BoundingBox']['Center']['@x'] = choose_default_value('x', graph)
        mutate_vehicle['BoundingBox']['Center']['@y'] = choose_default_value('y', graph)
        mutate_vehicle['BoundingBox']['Dimensions']['@width'] = choose_default_value('width', graph)
        mutate_vehicle['BoundingBox']['Dimensions']['@length'] = choose_default_value('length', graph)
        mutate_vehicle['BoundingBox']['Dimensions']['@height'] = choose_default_value('height', graph)
        mutate_vehicle['@vehicleCategory'] = random.choice(['bicycle', 'bus', 'car', 'motorbike', 'semitrailer', 'trailer', 'truck', 'van'])
        mutate_vehicle['@role'] = choose_default_value('role', graph)
        mutate_vehicle['Performance']['@maxAcceleration'] = choose_default_value('maxAcceleration', graph)
        mutate_vehicle['Performance']['@maxAccelerationRate'] = choose_default_value('maxAccelerationRate', graph)
        mutate_vehicle['Performance']['@maxDeceleration'] = choose_default_value('maxDeceleration', graph)
        mutate_vehicle['Performance']['@maxDecelerationRate'] = choose_default_value('maxDecelerationRate', graph)
        mutate_vehicle['Performance']['@maxSpeed'] = choose_default_value('maxSpeed', graph)

    data = xmlparser.xml2dict(catalog_location_path)
    vehicle_object = data['CatalogDefinition']['Catalog']['Vehicle']
    if type(vehicle_object) is dict:
        mutate(vehicle_object)
    elif type(vehicle_object) is list:
        for single_object in vehicle_object:
            mutate(single_object)
    xmlparser.dict2xml(data, catalog_location_path)


def mutate_pedestrain(catalog_location_path: str, graph):
    """
    变异Catalog中的Pedestrain
    """
    def mutate(mutate_pedestrain: dict):
        mutate_pedestrain['@mass'] = choose_default_value('mass', graph)
        mutate_pedestrain['BoundingBox']['Center']['@x'] = choose_default_value('x', graph)
        mutate_pedestrain['BoundingBox']['Center']['@y'] = choose_default_value('y', graph)
        mutate_pedestrain['BoundingBox']['Dimensions']['@width'] = choose_default_value('width', graph)
        mutate_pedestrain['BoundingBox']['Dimensions']['@length'] = choose_default_value('length', graph)
        mutate_pedestrain['BoundingBox']['Dimensions']['@height'] = choose_default_value('height', graph)
        mutate_pedestrain['@pedestrainCategory'] = choose_default_value('pedestrainCategory', graph)
        mutate_pedestrain['@role'] = choose_default_value('role', graph)
        
    data = xmlparser.xml2dict(catalog_location_path)
    misc_object = data['CatalogDefinition']['Catalog']['Pedestrain']
    if type(misc_object) is dict:
        mutate(misc_object)
    elif type(misc_object) is list:
        for single_object in misc_object:
            mutate(single_object)
    xmlparser.dict2xml(data, catalog_location_path)

def mutate_misc_object(catalog_location_path: str, graph):
    """
    变异Catalog中的MiscObject
    """
    def mutate(mutate_object: dict):
        mutate_object['Center']['@x'] = choose_default_value('x', graph)
        mutate_object['Center']['@y'] = choose_default_value('y', graph)
        mutate_object['Dimensions']['@width'] = choose_default_value('width', graph)
        mutate_object['Dimensions']['@length'] = choose_default_value('length', graph)
        mutate_object['Dimensions']['@height'] = choose_default_value('height', graph)
    
    data = xmlparser.xml2dict(catalog_location_path)
    misc_object = data['CatalogDefinition']['Catalog']['MiscObject']
    if type(misc_object) is dict:
        mutate(misc_object['BoundingBox'])
    elif type(misc_object) is list:
        for single_object in misc_object:
            mutate(single_object['BoundingBox'])
    xmlparser.dict2xml(data, catalog_location_path)

def mutate_xodr(xodr_path: str, graph):
    '''
    变异xodr中的signal和object
    '''
    def mutate_obstacle(data: dict):
        data['@width'] = choose_default_value('width', graph)
        data['@length'] = choose_default_value('length', graph)
        data['@height'] = choose_default_value('height', graph)

    def mutate_signal(data: dict):
        data['@value'] = random.uniform(10, 200)

    data = xmlparser.xml2dict(xodr_path)
    if 'signals' in data['OpenDRIVE']['road']:
        for signal in data['OpenDRIVE']['road']['signals']:
            mutate_signal(signal)
    if 'objects' in data['OpenDRIVE']['road']:
        for single_object in data['OpenDRIVE']['road']['objects']:
            if single_object['@type'] == 'obstacle':
                mutate_obstacle(single_object)

    xmlparser.dict2xml(data, xodr_path)

def mutate_weather(data: dict, graph):
    """
    变异weather
    """
    data['Sun']['@illuminance'] = choose_default_value('illuminance', graph)
    data['Fog']['@visualRange'] = choose_default_value('visualRange', graph)
    data['Fog']['BoundingBox']['Center']['@x'] = choose_default_value('x', graph)
    data['Fog']['BoundingBox']['Center']['@y'] = choose_default_value('y', graph)
    data['Fog']['BoundingBox']['Dimensions']['@width'] = choose_default_value('width', graph)
    data['Fog']['BoundingBox']['Dimensions']['@length'] = choose_default_value('length', graph)
    data['Fog']['BoundingBox']['Dimensions']['@height'] = choose_default_value('height', graph)
    data['Precipitation']['@precipitationIntensity'] = choose_default_value('precipitationIntensity', graph)
    data['Wind']['@direction'] = choose_default_value('direction', graph)
    data['Wind']['@speed'] = choose_default_value('speed', graph)


def mutate(file_path: str, result_path: str, graph):
    data = xmlparser.xml2dict(file_path)

    # 变异Catalog里的Vehicle
    if 'VehicleCatalogLocation' in data['OpenScenario']['CatalogLocations']:
        mutate_vehicle(data['OpenScenario']['CatalogLocations']['VehicleCatalogLocation']['Directory']['@path'], graph)

    # 变异Catalog里的Pedestrain
    if 'PedestrainCatalogLocation' in data['OpenScenario']['CatalogLocations']:
        mutate_pedestrain(data['OpenScenario']['CatalogLocations']['PedestrainCatalogLocation']['Directory']['@path'], graph)

    # 变异Catalog里的MiscObject
    if "MiscObjectCatalogLocation" in data['OpenScenario']['CatalogLocations']:
        mutate_misc_object(data['OpenScenario']['CatalogLocations']['MiscObjectCatalogLocation']['Directory']['@path'], graph)
    
    # 变异xodr里的obstacle和signal
    if "@filepath" in data['OpenScenario']['RoadNetwork']['File']:
        mutate_xodr(data['OpenScenario']['RoadNetwork']['File']['@path'], graph)

    # 变异xosc里的Weather
    weather = data['OpenScenario']['Storyboard']['Init']['InitActions']['GlobalAction']['EnvironmentAction']['Environment']['Weather']
    mutate_weather(weather, graph)
    xmlparser.dict2xml(data, result_path)
    validate_file(result_path)


if __name__ == '__main__':
    uri = "bolt://localhost:7687"
    username = "neo4j"
    password = "12345678"
    graph = Graph(uri, auth=(username, password))
    mutate('Mutate/CutIn.xosc', 'Mutate/CutIn-mutate.xosc', 'visualRange', graph, 'row')