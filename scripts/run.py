import argparse
import symeess


parser = argparse.ArgumentParser(description='Symeess')

parser.add_argument('input_file', type=str, help='input file name(+extension)')
parser.add_argument('-o', '-output', dest='output_name', default=None, help='output_name')

# Shape input flags
group_shape = parser.add_argument_group('Shape', 'Shape_options')
group_shape.add_argument('-m', '--measure', action='store_true', default=False,
                         help='Shape measure of input structure with reference polyhedra')
group_shape.add_argument('-s', '--structure', action='store_true', default=False,
                         help='Calculate the ideal structure for the input structure')
group_shape.add_argument('-t', '--test', action='store_true', default=False,
                         help='Print the reference structure of the given label')
group_shape.add_argument('-c', action='store', type=int, default=None,
                         help='Position of the central atom if exist')
group_shape.add_argument('-label', dest='reference_polyhedra', action='store',  default=None,
                         help='Use labels from Shape manual for desire reference polyhedra')


args = parser.parse_args(['-mst', '-label', 'T-4 SP-4',
                          '-c', '1',
                          '-o', '../examples/coord.dat',
                          '../examples/coord.cor'])

if args.measure or args.structure or args.test:
    if args.reference_polyhedra is None:
        print('Error. Shape needs a structure reference to compare')
        exit()
    symeess.Symeess(args.input_file, shape_label=args.reference_polyhedra,
                    shape_options=(args.structure, args.measure, args.test, args.c), output_name=args.output_name)
