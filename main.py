#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
from pathlib import Path
from shapely import geometry
import json
from lxml import etree


# path
GRAPH_FILEPATH = Path(__file__).with_name('s3_cure.xml')
TMP_GRAPH_FILE = Path(__file__).with_name('scene_graph.xml')
GPT_BIN_PATH = Path('C:\Program Files\snap\\bin\gpt')
OUTPUT_PATH = Path('C:\Michal\gisat\projects\Cure\S3\output')
INPUT_PATH = Path('C:\Michal\gisat\projects\Cure\S3')
DATA_PATH = Path('C:\\Users\micha\PycharmProjects\GEO\GISAT\cure\Sen3creo')

# gpt setting
GPT_MAX_PARALLEL = 1
GPT_TIMEOUT = 2 * 3600

# xml
with open(GRAPH_FILEPATH, 'r') as file:
    graph = etree.fromstring(file.read())


data_test = {
    "S3B_SL_1_RBT____20201206T203756_20201206T204056_20201208T011623_0179_046_271_0720_LN2_O_NT_004.SEN3": {
        "id": "C:\Michal\gisat\projects\Cure\S3\S3B_SL_1_RBT____20201206T203756_20201206T204056_20201208T011623_0179_046_271_0720_LN2_O_NT_004.SEN3",
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [
                        23.1698,
                        54.496
                    ],
                    [
                        22.3789,
                        54.4636
                    ],
                    [
                        21.6045,
                        54.4071
                    ],
                    [
                        20.8123,
                        54.3678
                    ],
                    [
                        20.0397,
                        54.3103
                    ],
                    [
                        19.2678,
                        54.248
                    ],
                    [
                        18.4915,
                        54.1799
                    ],
                    [
                        17.725,
                        54.1101
                    ],
                    [
                        16.9477,
                        54.0429
                    ],
                    [
                        16.192,
                        53.9613
                    ],
                    [
                        15.4358,
                        53.8704
                    ],
                    [
                        14.6721,
                        53.7869
                    ],
                    [
                        13.9071,
                        53.692
                    ],
                    [
                        13.1506,
                        53.5926
                    ],
                    [
                        12.407,
                        53.4883
                    ],
                    [
                        11.6557,
                        53.3803
                    ],
                    [
                        10.9222,
                        53.2682
                    ],
                    [
                        10.1869,
                        53.152
                    ],
                    [
                        9.45673,
                        53.0225
                    ],
                    [
                        8.71568,
                        52.8955
                    ],
                    [
                        7.99687,
                        52.7668
                    ],
                    [
                        7.27951,
                        52.6338
                    ],
                    [
                        6.56257,
                        52.4959
                    ],
                    [
                        5.84333,
                        52.3518
                    ],
                    [
                        5.14775,
                        52.2003
                    ],
                    [
                        4.44118,
                        52.0505
                    ],
                    [
                        3.73841,
                        51.8855
                    ],
                    [
                        3.04715,
                        51.7336
                    ],
                    [
                        2.35399,
                        51.5641
                    ],
                    [
                        1.68003,
                        51.3922
                    ],
                    [
                        1.41143,
                        51.3285
                    ],
                    [
                        2.9442,
                        48.8316
                    ],
                    [
                        4.35817,
                        46.2743
                    ],
                    [
                        5.64974,
                        43.7014
                    ],
                    [
                        6.83793,
                        41.1152
                    ],
                    [
                        7.06366,
                        41.172
                    ],
                    [
                        7.64028,
                        41.3112
                    ],
                    [
                        8.22036,
                        41.4515
                    ],
                    [
                        8.7997,
                        41.5895
                    ],
                    [
                        9.39127,
                        41.7215
                    ],
                    [
                        9.97917,
                        41.8588
                    ],
                    [
                        10.5733,
                        41.9851
                    ],
                    [
                        11.161,
                        42.1058
                    ],
                    [
                        11.7551,
                        42.2253
                    ],
                    [
                        12.3593,
                        42.3437
                    ],
                    [
                        12.9605,
                        42.4655
                    ],
                    [
                        13.5576,
                        42.5762
                    ],
                    [
                        14.1621,
                        42.6844
                    ],
                    [
                        14.7617,
                        42.7888
                    ],
                    [
                        15.3741,
                        42.8903
                    ],
                    [
                        15.9913,
                        42.9881
                    ],
                    [
                        16.5973,
                        43.0842
                    ],
                    [
                        17.2176,
                        43.1834
                    ],
                    [
                        17.8264,
                        43.2688
                    ],
                    [
                        18.4509,
                        43.3523
                    ],
                    [
                        19.0684,
                        43.4344
                    ],
                    [
                        19.6835,
                        43.5228
                    ],
                    [
                        20.3137,
                        43.591
                    ],
                    [
                        20.9388,
                        43.6632
                    ],
                    [
                        21.5564,
                        43.7322
                    ],
                    [
                        22.1808,
                        43.8009
                    ],
                    [
                        22.8076,
                        43.866
                    ],
                    [
                        23.4396,
                        43.9326
                    ],
                    [
                        24.0726,
                        43.9781
                    ],
                    [
                        24.7044,
                        44.0301
                    ],
                    [
                        24.307,
                        46.6598
                    ],
                    [
                        23.9174,
                        49.288
                    ],
                    [
                        23.5361,
                        51.9146
                    ],
                    [
                        23.1698,
                        54.496
                    ]
                ]
            ]
        }
    },
    "S3B_SL_1_RBT____20191214T085307_20191214T085607_20191215T141355_0179_033_164_1980_LN2_O_NT_003.SEN3": {
        "id": "/eodata/Sentinel-3/SLSTR/SL_1_RBT/2019/12/14/S3B_SL_1_RBT____20191214T085307_20191214T085607_20191215T141355_0179_033_164_1980_LN2_O_NT_003.SEN3",
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [
                        12.4142,
                        52.4703
                    ],
                    [
                        13.1612,
                        52.4282
                    ],
                    [
                        13.9169,
                        52.3795
                    ],
                    [
                        14.6643,
                        52.3192
                    ],
                    [
                        15.4002,
                        52.2685
                    ],
                    [
                        16.1325,
                        52.2126
                    ],
                    [
                        16.8704,
                        52.1471
                    ],
                    [
                        17.612,
                        52.0694
                    ],
                    [
                        18.3445,
                        51.9992
                    ],
                    [
                        19.0836,
                        51.9155
                    ],
                    [
                        19.8107,
                        51.8292
                    ],
                    [
                        20.5336,
                        51.7469
                    ],
                    [
                        21.2477,
                        51.6502
                    ],
                    [
                        21.9658,
                        51.5612
                    ],
                    [
                        22.6904,
                        51.4508
                    ],
                    [
                        23.3975,
                        51.3466
                    ],
                    [
                        24.113,
                        51.2341
                    ],
                    [
                        24.8135,
                        51.1208
                    ],
                    [
                        25.5167,
                        51.0011
                    ],
                    [
                        26.2155,
                        50.8867
                    ],
                    [
                        26.9184,
                        50.7574
                    ],
                    [
                        27.6046,
                        50.626
                    ],
                    [
                        28.2911,
                        50.4895
                    ],
                    [
                        28.9684,
                        50.3491
                    ],
                    [
                        29.6517,
                        50.2033
                    ],
                    [
                        30.3269,
                        50.0635
                    ],
                    [
                        30.9952,
                        49.9064
                    ],
                    [
                        31.6695,
                        49.7457
                    ],
                    [
                        32.3282,
                        49.5982
                    ],
                    [
                        32.9867,
                        49.4355
                    ],
                    [
                        33.2437,
                        49.3707
                    ],
                    [
                        34.8101,
                        51.863
                    ],
                    [
                        36.584,
                        54.3745
                    ],
                    [
                        38.5797,
                        56.8579
                    ],
                    [
                        40.8477,
                        59.3066
                    ],
                    [
                        40.524,
                        59.3795
                    ],
                    [
                        39.7222,
                        59.5855
                    ],
                    [
                        38.9171,
                        59.7835
                    ],
                    [
                        38.0931,
                        59.9744
                    ],
                    [
                        37.2511,
                        60.1674
                    ],
                    [
                        36.4143,
                        60.3444
                    ],
                    [
                        35.5541,
                        60.525
                    ],
                    [
                        34.7005,
                        60.6978
                    ],
                    [
                        33.8271,
                        60.8655
                    ],
                    [
                        32.9495,
                        61.0266
                    ],
                    [
                        32.0482,
                        61.1843
                    ],
                    [
                        31.1519,
                        61.3337
                    ],
                    [
                        30.2416,
                        61.4783
                    ],
                    [
                        29.3316,
                        61.6144
                    ],
                    [
                        28.4162,
                        61.7432
                    ],
                    [
                        27.4722,
                        61.8712
                    ],
                    [
                        26.5383,
                        61.988
                    ],
                    [
                        25.5941,
                        62.0973
                    ],
                    [
                        24.6513,
                        62.1961
                    ],
                    [
                        23.6932,
                        62.2999
                    ],
                    [
                        22.7295,
                        62.3948
                    ],
                    [
                        21.7504,
                        62.4731
                    ],
                    [
                        20.7677,
                        62.5606
                    ],
                    [
                        19.7991,
                        62.6279
                    ],
                    [
                        18.8117,
                        62.6889
                    ],
                    [
                        17.8129,
                        62.7546
                    ],
                    [
                        16.8201,
                        62.8055
                    ],
                    [
                        15.8242,
                        62.8493
                    ],
                    [
                        14.8501,
                        62.8793
                    ],
                    [
                        13.8245,
                        62.9155
                    ],
                    [
                        13.4886,
                        60.2955
                    ],
                    [
                        13.1393,
                        57.6741
                    ],
                    [
                        12.7786,
                        55.0512
                    ],
                    [
                        12.4142,
                        52.4703
                    ]
                ]
            ]
        }
    }
}

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
    if not output_path.exists():
        output_path.mkdir(parents=True, exist_ok=True)
    output_path_tag = graph.xpath('.//geoRegion[text()="aoi_wkt"]')
    output_path_tag[0].text = str(aoi)
    with open(TMP_GRAPH_FILE, 'w') as file:
        file.write(etree.tostring(graph, encoding='unicode', pretty_print=True))



for city, bbox in cities.items():
    with open(DATA_PATH / f'{city}.json', 'r') as file:
        data = json.load(file)

    aoi = geometry.box(*bbox)
    scenes = {name: properties for page in data.values() for name, properties in page.items() if is_within(bbox, properties.get('geometry'))
                and name.find('_NT_') > 1}

    for name, properties in scenes.items():
        scene_path = Path(properties.get('id'))
        build_graph(scene_path, OUTPUT_PATH / city / f'{name}.tif', aoi.to_wkt())

        args = [str(GPT_BIN_PATH),
                str(TMP_GRAPH_FILE),
                "-e",
                "-q", str(GPT_MAX_PARALLEL)]
        pr = subprocess.run(args, check=False)
        pr.check_returncode()










        print()


# log = logging.getLogger(__name__)
#
#
# class NoOverlapException(Exception):
#     pass
#
#
# def clean_zero_locations(src_filepath, dst_filepath, nodata_value):
#     # Read band into an array.
#     src_dset = gdal.Open(str(src_filepath), GA_ReadOnly)
#     log.debug("Cleaning zero locations, dataset size is {} x {}.".format(src_dset.RasterXSize, src_dset.RasterYSize))
#     band_arr = src_dset.GetRasterBand(1).ReadAsArray()
#
#     # Clean zero locations.
#     coords = numpy.stack(numpy.nonzero(band_arr == 0), axis=1)
#     for (y, x) in coords:
#         band_arr[(y-CLEAN_SIZE):(y+CLEAN_SIZE),(x-CLEAN_SIZE):(x+CLEAN_SIZE)] = nodata_value
#
#     # Save the band into destination file.
#     driver = gdal.GetDriverByName("GTiff")
#     dst_dset = driver.Create(str(dst_filepath),
#                              src_dset.RasterXSize,
#                              src_dset.RasterYSize,
#                              1,
#                              src_dset.GetRasterBand(1).DataType,
#                              ["COMPRESS=DEFLATE", "TILED=YES"])
#     dst_dset.SetGeoTransform(src_dset.GetGeoTransform())
#     dst_dset.SetProjection(src_dset.GetProjection())
#     dst_dset.GetRasterBand(1).WriteArray(band_arr)
#     dst_dset.GetRasterBand(1).SetNoDataValue(nodata_value)
#
#
# def has_overlap_error(log_filepath):
#     with open(log_filepath, "rt") as logf:
#         for line in logf:
#             if OVERLAP_ERROR_RE.search(line) is not None:
#                 return True
#     return False
#
#
# def generate_backscatter(manifest_filepath, result_basename, work_dir, log_filepath, polarisation, rel_orbit_number, aoi_wkt=None):
#     result_filepaths = []
#
#     if aoi_wkt is None:
#         graph_filepath = BACKSCATTER_GRAPH_FILEPATH
#     else:
#         graph_filepath = BACKSCATTER_AOI_GRAPH_FILEPATH
#     log.debug("Using gpt graph {:s}.".format(str(graph_filepath)))
#
#     # Let gpt generate backscatter.
#     #
#     # NOTE:
#     # Do not use -c switch, while it collides somehow with -Xmx jvm option.
#     result1_filepath = work_dir.joinpath("{:s}.gpt.tif".format(result_basename))
#     args = [str(GPT_BIN_PATH),
#             str(graph_filepath),
#             "-e",
#             "-x",
#             "-q", str(GPT_MAX_PARALLEL),
#             "-Ppolarisation={:s}".format(polarisation),
#             "-Psource={:s}".format(str(manifest_filepath)),
#             "-Ptarget={:s}".format(str(result1_filepath))]
#     if aoi_wkt is not None:
#         args.append("-Paoi_wkt={:s}".format(aoi_wkt))
#     log.debug("Starting generating backscatter {:s}.".format(result_basename))
#     try:
#         log_subprocess(args, work_dir, log_filepath, GPT_TIMEOUT)
#     except subprocess.CalledProcessError:
#         if has_overlap_error(log_filepath):
#             raise NoOverlapException("Scene {:s} does not overlap the aoi.".format(str(manifest_filepath)))
#         else:
#             raise
#     log.debug("The snap generated backscatter to {:s}.".format(str(result1_filepath)))
#
#     # Clean zero locations.
#     result2_filepath = work_dir.joinpath("{:s}.tif".format(result_basename))
#     clean_zero_locations(result1_filepath, result2_filepath, NODATA_VALUE)
#     log.info("Backscatter has been cleaned and saved to {:s}.".format(str(result2_filepath)))
#     result_filepaths.append(result2_filepath)
#     result1_filepath.unlink()
#
#     # Create report file.
#     report_text = "".join(["Type: Backscatter\n",
#                            "Manifest: {:s}\n".format(str(manifest_filepath)),
#                            "Polarisation: {:s}\n".format(polarisation),
#                            "Orbit: {:d}\n".format(rel_orbit_number),
#                            "Cmd: {:s}\n".format(repr(args))])
#     report_filepath = work_dir.joinpath("{:s}.report.txt".format(result_basename))
#     report_filepath.write_text(report_text)
#     log.info("Report file has been saved to {:s}.".format(str(report_filepath)))
#     result_filepaths.append(report_filepath)
#
#     return result_filepaths