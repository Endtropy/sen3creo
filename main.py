#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
from pathlib import Path
from shapely import geometry
import json
from lxml import etree
import time
import datetime
# path
GRAPH_FILEPATH = Path(__file__).with_name('s3_cure.xml')
TMP_GRAPH_FILE = Path(__file__).with_name('scene_graph.xml')
GPT_BIN_PATH = Path('C:\Program Files\snap\\bin\gpt')
OUTPUT_PATH = Path('C:\Michal\gisat\projects\Cure\S3\output')
INPUT_PATH = Path('C:\Michal\gisat\projects\Cure\S3')
DATA_PATH = Path('C:\\Users\micha\PycharmProjects\GEO\GISAT\cure\Sen3creo')

# gpt setting
GPT_MAX_PARALLEL = 2
GPT_TIMEOUT = 2 * 3600

# count
N_SCENE = 0

BATCH = {}

# xml
with open(GRAPH_FILEPATH, 'r') as file:
    graph = etree.fromstring(file.read())

cities = { 'berlin': [12.0, 53.5, 14.5, 51.5],
           'copenhagen': [11.6, 56.2, 12.8, 55.3],
           'heraklion': [24.8, 35.5, 25.4, 35.1],
           'sofia': [22.7, 43.2, 24.1, 42.1]}

def is_within(geo1,geo2):
    shape1 = geometry.box(*geo1)
    shape2 = geometry.shape(geo2)
    return shape2.contains(shape1)

def build_graph(scene_path, output_path, aoi):
    scene_path_tag = graph.xpath('.//file[text()="scene_path"]')
    scene_path_tag[0].text = str(scene_path / 'xfdumanifest.xml')
    output_path_tag = graph.xpath('.//file[text()="output_path"]')
    output_path_tag[0].text = str(output_path)
    if not output_path.parent.exists():
        output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path_tag = graph.xpath('.//geoRegion[text()="aoi_wkt"]')
    output_path_tag[0].text = str(aoi)
    with open(TMP_GRAPH_FILE, 'w') as file:
        file.write(etree.tostring(graph, encoding='unicode', pretty_print=True))


start_proc = time.perf_counter()

# job pref
for city, bbox in cities.items():
    with open(DATA_PATH / f'{city}.json', 'r') as file:
        data = json.load(file)
    scenes = {name: properties for page in data.values() for name, properties in page.items() if is_within(bbox, properties.get('geometry'))
                and name.find('_NT_') > 1}
    N_SCENE += len(scenes)
    BATCH.update({city: scenes})

print(f'{N_SCENE} to process')
i = 1


for city, scenes in BATCH.items():
    bbox = cities.get(city)
    aoi = geometry.box(*bbox)
    for name, properties in scenes.items():
        start_scene = time.perf_counter()

        scene_path = INPUT_PATH  / Path(properties.get('id')).lstrip('/eodata/')
        build_graph(scene_path, OUTPUT_PATH / city / f'{name.rstrip(".SEN3")}.tif', aoi.to_wkt())

        args = [str(GPT_BIN_PATH),
                str(TMP_GRAPH_FILE),
                "-e",
                "-q", str(GPT_MAX_PARALLEL)]
        pr = subprocess.run(args, check=False)
        pr.check_returncode()

        end_scene = time.perf_counter()
        end_proc = time.perf_counter()

        print(f'{name}: {i}/{N_SCENE} '
              f'\n scene procesed in:{end_scene-start_scene} '
              f'\n estimation: {(end_scene-start_scene)*(N_SCENE-i)/60} min'
              f'\n finished at: {datetime.datetime.now() + datetime.timedelta(seconds=(end_scene-start_scene)*(N_SCENE-i))}')
        i += 1
