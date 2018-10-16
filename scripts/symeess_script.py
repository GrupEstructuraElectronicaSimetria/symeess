#!/usr/bin/env python
import argparse
import symeess
import sys


parser = argparse.ArgumentParser(description='Symeess')
parser.add_argument('-input_file', type=str, default=None, help='input file name(+extension)')
parser.add_argument('-o', '-output', dest='output_name', default=None, help='customize output file name')

# Shape input flags
group_shape = parser.add_argument_group('Shape')
group_shape.add_argument('-m', '--measure',
                         action='store_true',
                         default=False,
                         help='return shape measure of input structure with reference polyhedra')
group_shape.add_argument('-s', '--structure',
                         action='store_true',
                         default=False,
                         help='calculate the ideal structure for the input structure')
group_shape.add_argument('-t', '--test',
                         action='store_true',
                         default=False,
                         help='print the reference structure of the given label')
group_shape.add_argument('-c', action='store',
                         type=int,
                         default=0,
                         help='position of the central atom if exist')
group_shape.add_argument('-label',
                         dest='reference_polyhedra',
                         action='store',
                         nargs='+',
                         default=None,
                         help='use labels from Shape manual for desire reference polyhedra')
group_shape.add_argument('-n',
                         action='store',
                         type=str,
                         default=None,
                         help='Print all the possible reference structures of n vertices')
group_shape.add_argument('-map',
                         action='store_true',
                         default=False,
                         help='Calculates the path deviation function for the minimal '
                              'distortion interconversion path between two given polyhedra')
group_shape.add_argument('-path',
                         action='store_true',
                         default=False,
                         help='Calculates generalized coordinate from the path deviation function for a given path')

# Symgroup input flags
group_symgroup = parser.add_argument_group('Symgroup')
group_symgroup.add_argument('-sym', '--symmetry', action='store_true', default=False,
                            help='Shape measure of input structure with reference polyhedra')
# group_symgroup.add_argument('-c', action='store', type=int, default=None,
#                             help='Position of the central atom if exist')
# group_symgroup.add_argument('-label', dest='symmetry_operation', action='store',  default=None,
#                             help='compute the symmetry operation for the given structure')


class Main():

    def __init__(self, arguments):

        self.args = parser.parse_args(arguments)

        if self.args.input_file is not None:
            molecules = symeess.file_io.read_input_file(self.args.input_file)
            self.symobj = symeess.Symeess()
            self.symobj.set_molecules(molecules)
        if self.args.output_name is not None:
            self.output_name = self.args.output_name
        else:
            self.output_name = 'symeess'

        self.shape()

    def shape(self):
        # Shape's commands

        central_atom = self.args.c
        reference_polyhedron = self.args.reference_polyhedra

        if self.args.structure:
            self.symobj.write_shape_structure_2file(reference_polyhedron,
                                                    central_atom=central_atom,
                                                    output_name=self.output_name)
        if self.args.measure:
            self.symobj.write_shape_measure_2file(reference_polyhedron,
                                                  central_atom=central_atom,
                                                  output_name=self.output_name)
        if self.args.test:
            for reference in reference_polyhedron:
                print(reference)
                for array in symeess.shape.shape_tools.get_test_structure(reference, central_atom=central_atom):
                    print('{:11.8f} {:11.8f} {:11.8f}'.format(array[0], array[1], array[2]))

        if self.args.n:
            print('Available reference structure with {} Vertices'.format(self.args.n))
            print(symeess.shape.shape_tools.get_structure_references(self.args.n))

        if self.args.map:
            symeess.write_minimum_distortion_path_shape_2file(reference_polyhedron[0],
                                                              reference_polyhedron[1],
                                                              num_points=20)
        if self.args.path:
            self.symobj.write_path_parameters_2file('SP-4', 'T-4',
                                                    central_atom=central_atom,
                                                    output_name=self.output_name)


if __name__ == '__main__':
    Main(sys.argv[1:])