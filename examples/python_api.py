import symeess.file_io as file_io
import symeess.shape as shape
import symeess.symmetry.symgroup as symgroup

def print_data(geometries):
    print('{:10} {:^10} {:^10} {:^10}'.format('name', 'SP-4', 'SS-4', 'PP-5'))
    print('-'*43)
    for geometry in geometries:
        print('{:10} {:^10.3f} {:^10.3f} {:^10.3f}'.format(geometry.get_name(),
                                                           geometry.get_shape_measure('SP-4', central_atom=1),
                                                           geometry.get_shape_measure('SS-4', central_atom=1),
                                                           geometry.get_shape_measure('PP-5')
                                                           ))
    print()


# Get structures from files
molecules_set = file_io.read_file_xyz('coord.xyz')
fragments_set = file_io.read_file_cor('coord.cor')

# Call shape as method of Geometry class
print_data(molecules_set)
print_data(fragments_set)


# Check multiple calls of shape one calculatioin
methane = molecules_set[0]
for i in range(100):
    measure = methane.get_shape_measure('SP-4', central_atom=1)

print('final measure:', measure)

# Call shape as method of Shape class (semi function call)
print('measure:', shape.Shape(methane).measure('SP-4', central_atom=1))
print('structure:\n', shape.Shape(methane).structure('SP-4', central_atom=1))

# test symgroup
print('\nSYMMETRY\n--------')

# Check multiple calls of symgroup one calculatioin
for i in range(100):
    measure = methane.get_symgroup_measure('C3', central_atom=1)

print('measure: {:^10.3f} '.format(measure))
print('measure: {:^10.3f} '.format(methane.get_symgroup_measure('C4', central_atom=1)))

# Call symgroup as method of Symgroup class (semi function call)
print('measure: {:^10.3f} '.format(symgroup.Symgroup(methane).measure('C4', central_atom=1)))
print(symgroup.Symgroup(methane).nearest_structure('C4', central_atom=1))


# test WFNSYM
print('\nWFNSYM\n--------')


molecule = file_io.read_input_file('pirrol.fchk')
data = molecule.electronic_structure.get_wfnsym_measure('Td',
                                                        VAxis1=[0.000000000, 0.000000000, 1.000000000],
                                                        VAxis2=[-2.027247, 0.000133, -0.898469],
                                                        RCread=[0.002440, -0.000122, 0.017307])

print(data.SymLab)
print(data.grim_coef)