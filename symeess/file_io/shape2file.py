import os
import sys


# def write_shape_data(data, shape_label, central_atom, option, output_name=sys.stdout):
#
#     extensions = {'measure': '.tab', 'structure': '.out', 'test': '.tst'}
#     if not os.path.exists('./results'):
#         os.makedirs('./results')
#     output = open('results/'+output_name + extensions[option], 'w')
#
#     output.write('-'*70 + '\n')
#     output.write('S H A P E v2.1 '
#                  'Continuous Shape Measures calculation\n'
#                  '(c) 2013 Electronic Structure Group,  Universitat de Barcelona\n'
#                  'Contact: llunell@ub.edu\n')
#     output.write('-'*70 + '\n')
#
#     if 'measure' in option:
#         output.write('{}'.format('Structure'))
#         for label in shape_label:
#             n = len(label) + 3
#             output.write('{}'.format(label.rjust(n)))
#         output.write('\n')
#         for idx, molecule_name in enumerate(data):
#             output.write('{}'.format(molecule_name.get_name()))
#             if molecule_name.get_name().strip() == '':
#                 n = 4 + len(molecule_name.get_name())
#             else:
#                 n = 14 - len(molecule_name.get_name())
#             for label in shape_label:
#                 output.write(' {:{width}.{prec}f}'.format(data[idx].geometry.get_shape_measure(label, central_atom),
#                                                           width=n, prec=3))
#                 n = 7
#             output.write('\n')
#
#     if 'structure' in option:
#         for idx, molecule_name in enumerate(data):
#             output.write('\n')
#             output.write('Structure {} : {}\n'.format(idx+1, molecule_name.get_name()))
#
#             for idn, array in enumerate(data[idx].geometry.get_positions()):
#                 output.write('{:2s}'.format(data[idx].geometry.get_symbols()[idn]))
#                 output.write(' {:11.7f} {:11.7f} {:11.7f}\n'.format(array[0], array[1], array[2]))
#
#             output.write('\n')
#
#             for label in shape_label:
#                 output.write('{} Ideal Structure CShM = {:.3f}\n'
#                              .format(label, data[idx].geometry.get_shape_measure(label, central_atom)))
#                 for idn, array in enumerate(data[idx].geometry.get_shape_structure(label, central_atom)):
#                     output.write('{:2s}'.format(data[idx].geometry.get_symbols()[idn]))
#                     output.write(' {:11.7f} {:11.7f} {:11.7f}\n'.format(array[0], array[1], array[2]))
#                 output.write('\n')
#
#             output.write('-' * 70 + '\n')
#
#     if 'test_structure' in option:
#         output.write("{}\n".format('test_structure'.upper()))
#         n = 20
#         for label in shape_label:
#             output.write('{}'.format(label.rjust(n)))
#             n = 36 + len(label)
#         output.write('\n')
#
#         for idx in list(range(len(data[0]['symbols']))):
#             for label in shape_label:
#                 array = data[0][label]['test_structure'][idx]
#                 output.write(' {:11.7f} {:11.7f} {:11.7f} |'.format(array[0], array[1], array[2]))
#             output.write('\n')
#
#     output.close()


def shape_header(output):
    output.write('-' * 70 + '\n')
    output.write('S H A P E v2.1 '
                 'Continuous Shape Measures calculation\n'
                 '(c) 2013 Electronic Structure Group,  Universitat de Barcelona\n'
                 'Contact: llunell@ub.edu\n')
    output.write('-' * 70 + '\n' + '\n')


def write_shape_measure_data(measures, molecules_name, shape_label, output_name=sys.stdout):

    if not os.path.exists('./results'):
        os.makedirs('./results')
    output = open('results/' + output_name + '.tab', 'w')
    if not os.path.exists('./results'):
        os.makedirs('./results')
    shape_header(output)

    output.write('{}'.format('Structure'))
    for label in shape_label:
        n = len(label) + 3
        output.write('{}'.format(label.rjust(n)))
    output.write('\n')
    for idx, name in enumerate(molecules_name):
        output.write('{}'.format(name))
        if name.strip() == '':
            n = 4 + len(name)
        else:
            n = 14 - len(name)
        for idn, label in enumerate(shape_label):
            output.write(' {:{width}.{prec}f}'.format(measures[idn][idx], width=n, prec=3))
            n = 7
        output.write('\n')
    output.close()

def write_shape_structure_data(initial_geometry, structures, measures, symbols,
                               molecules_name, shape_label, output_name=sys.stdout):

    if not os.path.exists('./results'):
        os.makedirs('./results')
    output = open('results/' + output_name + '.out', 'w')
    shape_header(output)

    for idx, name in enumerate(molecules_name):
        output.write('\n')
        output.write('Structure {} : {}\n'.format(idx+1, name))

        for idn, array in enumerate(initial_geometry[idx]):
            output.write('{:2s}'.format(symbols[idx][idn]))
            output.write(' {:11.7f} {:11.7f} {:11.7f}\n'.format(array[0], array[1], array[2]))
        output.write('\n')

        for idn, label in enumerate(shape_label):
            output.write('{} Ideal Structure CShM = {:.3f}\n'
                         .format(label, measures[idn][idx]))
            for jd, array in enumerate(structures[idn][idx]):
                output.write('{:2s}'.format(symbols[idx][jd]))
                output.write(' {:11.7f} {:11.7f} {:11.7f}\n'.format(array[0], array[1], array[2]))
            output.write('\n')

        output.write('-' * 70 + '\n')
    output.close()


def write_shape_map(shape_label1, shape_label2, path, output_name='symeess_shape_map'):

    if not os.path.exists('./results'):
        os.makedirs('./results')
    output = open('results/' + output_name + '.pth', 'w')
    shape_header(output)

    output.write(" {:6} {:6}\n".format(shape_label1, shape_label2))
    for idx, value in enumerate(path[0]):
        output.write('{:6.3f} {:6.3f}'.format(path[0][idx], path[1][idx]))
        output.write('\n')
    output.close()


def write_minimal_distortion_path_analysis(shape_label1, shape_label2, measures, pathdev, GenCoord,
                                           maxdev, mindev, mingco, maxgco, molecule_names,
                                           output_name='symeess_shape'):

    if not os.path.exists('./results'):
        os.makedirs('./results')
    output = open('results/' + output_name + '.flt', 'w')
    shape_header(output)

    output.write("Deviation threshold to calculate Path deviation function: "
                 "{:2.1f}% - {:2.1f}%\n".format(mindev, maxdev))
    output.write("Deviation threshold to calculate Generalized Coordinate: "
                 "{:2.1f}% - {:2.1f}%\n".format(mingco, maxgco))
    output.write("\n")
    output.write('{:11}'.format('structure'.upper()))
    output.write(" {:7} {:7}".format(shape_label1, shape_label2))
    output.write("{:6} {:6}".format('DevPath', 'GenCoord'))
    output.write("\n")

    for idx, molecule_name in enumerate(molecule_names):
        output.write('{}'.format(molecule_name))
        if molecule_names[idx].strip() == '':
            n = 4 + len(molecule_names[idx])
        else:
            n = 15 - len(molecule_names[idx])
        for label in [shape_label1, shape_label2]:
            output.write(' {:{width}.{prec}f}'.format(measures[label][idx], width=n, prec=3))
            n = 7
        output.write('{:8.1f} {:8}'.format(pathdev[idx], GenCoord[idx]))
        output.write('\n')
    output.close()
