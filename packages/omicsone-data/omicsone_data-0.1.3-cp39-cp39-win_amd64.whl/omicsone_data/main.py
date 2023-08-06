import argparse
import sys, os, re

import numpy as np
import pandas as pd
from tqdm import tqdm

try:
    from plugins.data import ProteomeData, GlycoproteomeData
    from plugins.param import Parameter
except:
    from .plugins.data import ProteomeData,GlycoproteomeData
    from .plugins.param import Parameter


class MyParser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)
        self.print_help()
        sys.exit(2)


def standardrize_file(input_path, param_path, outdir_path):
    param = Parameter(param_path)
    folder, bn = os.path.split(input_path)
    bn, ext = os.path.splitext(bn)

    output_path = outdir_path + os.sep + bn + "-OmicsOneData.txt"
    p = None
    if param['type'] == 'proteome':
        p = ProteomeData(input_path)
    elif param['type'] == 'glycoproteome':
        p = GlycoproteomeData(input_path)

    df = p.data

    if int(param['idmap_run']) == 1:
        df = p.idmap(param)
    df.to_csv(output_path, sep="\t")


def build_id_map(input_path, output_dir):
    folder, bn = os.path.split(input_path)
    bn, ext = os.path.splitext(bn)

    df = pd.read_excel(input_path, engine='openpyxl')
    rows = []
    for index, row in df.iterrows():
        tumor_code = row['tumor_code']
        tumor_sample_id = row['tumor_sample_id']
        normal_sample_id = row['normal_sample_id']
        aliquout_normal = row['specimen/aliquout_id_protein_normal']
        aliquout_tumor = row['specimen/aliquout_id_protein_tumor']
        in_published_paper = row['in_published_paper']
        index = row['INDEX']
        rows.append([index, tumor_code, tumor_sample_id, aliquout_tumor, in_published_paper])
        rows.append([index, tumor_code, normal_sample_id, aliquout_normal, in_published_paper])

    output_path = output_dir + os.sep + bn + "-idMap.tsv"
    rdf = pd.DataFrame(rows, columns=['Index', 'tumor_code', 'sample_id', 'aliquout', 'in_published_paper'])
    rdf.to_csv(output_path, sep="\t", index=False)


def build_id_map_standalone():
    parser = MyParser(description='OmicsOne-data: build ID mapping table')
    parser.add_argument('-i', dest="input_file",
                        help="input file")
    parser.add_argument('-o', dest='output_dir', help='output directory')
    # parser.add_argument('-p', dest='param_file', help='parameter file (.param)')

    args = parser.parse_args()

    # check inputs
    if args.input_file is None or (not os.path.exists(args.input_file)):
        print('invalid input file')
        parser.print_help()
        sys.exit(1)
    if args.output_dir is None or (not os.path.exists(args.output_dir)):
        print('invalid output directory')
        parser.print_help()
        sys.exit(1)
    # if args.param_file is None or (not os.path.exists(args.param_file)):
    #     print('invalid parameter file')
    #     parser.print_help()
    #     sys.exit(1)
    build_id_map(input_path=args.input_file, output_dir=args.output_dir)


def main():
    parser = MyParser(description='OmicsOne-data: data reader and converter for omics data analysis')
    parser.add_argument('-i', dest="input_file",
                        help="input file")
    parser.add_argument('-o', dest='output_dir', help='output directory')
    parser.add_argument('-p', dest='param_file', help='parameter file (.param)')

    args = parser.parse_args()

    # check inputs
    if args.input_file is None or (not os.path.exists(args.input_file)):
        print('invalid input file')
        parser.print_help()
        sys.exit(1)
    if args.output_dir is None or (not os.path.exists(args.output_dir)):
        print('invalid output directory')
        parser.print_help()
        sys.exit(1)
    if args.param_file is None or (not os.path.exists(args.param_file)):
        print('invalid parameter file')
        parser.print_help()
        sys.exit(1)

    standardrize_file(input_path=args.input_file, param_path=args.param_file, outdir_path=args.output_dir)


if __name__ == "__main__":
    main()
