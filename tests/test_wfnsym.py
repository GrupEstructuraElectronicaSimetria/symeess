import unittest
from cosym import file_io
from numpy import testing


class TestWfnsym(unittest.TestCase):

    def setUp(self):
        self.structures = file_io.read_input_file('data/wfnsym/tih4_5d.fchk')
        self.wfnsym = self.structures[0].get_mo_symmetry('Td', vector_axis1=[0., 0., 1.],
                                                         vector_axis2=[-0.471418708, -0.816488390, -0.333333333],
                                                         center=[0., 0., 0.])

    def test_symmetry_overlap_analysis(self):
        td_labels = ['E', '2C3', '2C3', '2C3', '2C3', 'C2', 'C2', 'C2', '2S4', '2S4', '2S4',
                     's_d', 's_d', 's_d', 's_d', 's_d', 's_d']
        td_ideal_gt = [[1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
                       [1., 1., 1., 1., 1., 1., 1., 1., -1., -1., -1., -1., -1., -1., -1., -1., -1.],
                       [2., -1., -1., -1., -1., 2., 2., 2., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
                       [3., 0., 0., 0., 0., -1., -1., -1., 1., 1., 1., -1., -1., -1., -1., -1., -1.],
                       [3., 0., 0., 0., 0., -1., -1., -1., -1., -1., -1., 1., 1., 1., 1., 1., 1.]]
        soevs_a = [[1.00000000e+00, 1.00000000e+00, 1.00000000e+00, 1.00000000e+00, 1.00000000e+00, 1.00000000e+00,
                    1.00000000e+00, 1.00000000e+00, 1.00000000e+00, 1.00000000e+00, 1.00000000e+00, 1.00000000e+00,
                    1.00000000e+00, 1.00000000e+00, 1.00000000e+00, 1.00000000e+00, 1.00000000e+00],
                   [9.99999993e-01, 9.99999993e-01, 9.99999993e-01, 9.99999993e-01, 9.99999993e-01, 9.99999993e-01,
                    9.99999993e-01, 9.99999993e-01, 9.99999993e-01, 9.99999993e-01, 9.99999993e-01, 9.99999993e-01,
                    9.99999993e-01, 9.99999993e-01, 9.99999993e-01, 9.99999993e-01, 9.99999993e-01],
                   [9.99999999e-01, -5.00000000e-01, 4.99982958e-01, 5.00017041e-01, -4.99999999e-01, -1.93043210e-05,
                    1.93034940e-05, -9.99999999e-01, -4.99990347e-01, -5.00009651e-01, -1.45209404e-10, 4.99973306e-01,
                    5.00026693e-01, -9.99999999e-01, 5.00007390e-01, 4.99992611e-01, 9.99999999e-01],
                   [1.00000000e+00, 2.97822684e-02, -2.01849576e-04, -2.35347284e-04, -2.93450716e-02, -9.99563299e-01,
                    -9.99562308e-01, 9.99125607e-01, -2.18350608e-04, -2.18845982e-04, -9.99562803e-01, 2.97987697e-02,
                    2.97657674e-02, 1.00000000e+00, -2.93620686e-02, -2.93280755e-02, 9.99125607e-01],
                   [1.00000000e+00, 4.70217732e-01, -4.99781109e-01, -4.99781694e-01, 5.29345071e-01, -4.17396890e-04,
                    -4.56995453e-04, -9.99125607e-01, -4.99791301e-01, -4.99771502e-01, -4.37196424e-04, 4.70227924e-01,
                    4.70207539e-01, 1.00000000e+00, 5.29354678e-01, 5.29335464e-01, -9.99125607e-01],
                   [1.00000000e+00, 1.00000000e+00, 1.00000000e+00, 1.00000000e+00, 1.00000000e+00, 1.00000000e+00,
                    1.00000000e+00, 1.00000000e+00, 1.00000000e+00, 1.00000000e+00, 1.00000000e+00, 1.00000000e+00,
                    1.00000000e+00, 1.00000000e+00, 1.00000000e+00, 1.00000000e+00, 1.00000000e+00],
                   [1.00000000e+00, 8.11652935e-01, -1.56194991e-01, -1.56209328e-01, -4.99248617e-01, -6.87602514e-01,
                    -6.87588848e-01, 3.75191364e-01, -1.56198743e-01, -1.56205576e-01, -6.87595682e-01, 8.11656687e-01,
                    8.11649184e-01, 1.00000000e+00, -4.99259202e-01, -4.99238033e-01, 3.75191362e-01],
                   [1.00000000e+00, -5.00000000e-01, 4.99980074e-01, 5.00019926e-01, -5.00000000e-01, -1.99353402e-05,
                    1.99344079e-05, -9.99999999e-01, -4.99990032e-01, -5.00009967e-01, -2.00029036e-10, 4.99970106e-01,
                    5.00029893e-01, -9.99999999e-01, 5.00009960e-01, 4.99990042e-01, 1.00000000e+00],
                   [9.99999999e-01, -3.11652936e-01, -3.43785082e-01, -3.43810598e-01, 9.99248616e-01, -3.12377550e-01,
                    -3.12431086e-01, -3.75191364e-01, -3.43811225e-01, -3.43784457e-01, -3.12404318e-01,
                    -3.11626793e-01, -3.11679077e-01, 9.99999999e-01, 9.99249242e-01, 9.99247991e-01, -3.75191362e-01],
                   [9.99999998e-01, 9.99999998e-01, 9.99999998e-01, 9.99999998e-01, 9.99999998e-01, 9.99999998e-01,
                    9.99999998e-01, 9.99999998e-01, 9.99999998e-01, 9.99999998e-01, 9.99999998e-01, 9.99999998e-01,
                    9.99999998e-01, 9.99999998e-01, 9.99999998e-01, 9.99999998e-01, 9.99999998e-01],
                   [1.00000000e+00, -5.00000000e-01, 5.00006995e-01, 4.99993003e-01, -5.00000000e-01, 7.00877618e-06,
                    -7.00820415e-06, -9.99999999e-01, -5.00003504e-01, -4.99996496e-01, 1.92050017e-10, 5.00010499e-01,
                    4.99989499e-01, -9.99999998e-01, 4.99996508e-01, 5.00003491e-01, 1.00000000e+00],
                   [1.00000000e+00, -4.63941485e-01, -2.42884406e-01, -2.42872258e-01, 9.49698149e-01, -5.14251683e-01,
                    -5.14234985e-01, 2.84866699e-02, -2.42874158e-01, -2.42882507e-01, -5.14243335e-01, -4.63951733e-01,
                    -4.63931236e-01, 9.99999998e-01, 9.49700050e-01, 9.49696250e-01, 2.84866692e-02],
                   [1.00000000e+00, 9.63941486e-01, -2.57122589e-01, -2.57120746e-01, -4.49698151e-01, -4.85755325e-01,
                    -4.85758006e-01, -2.84866702e-02, -2.57122338e-01, -2.57120998e-01, -4.85756665e-01, 9.63941235e-01,
                    9.63941737e-01, 1.00000000e+00, -4.49696559e-01, -4.49699742e-01, -2.84866697e-02],
                   [1.00000000e+00, -5.00000001e-01, 4.99992959e-01, 5.00007041e-01, -5.00000000e-01, -7.25146649e-06,
                    7.25125701e-06, -1.00000000e+00, -4.99996375e-01, -5.00003626e-01, -7.70465682e-12, 4.99989333e-01,
                    5.00010667e-01, -1.00000000e+00, 5.00003416e-01, 4.99996585e-01, 1.00000000e+00],
                   [1.00000000e+00, -2.46500289e-01, -1.81658885e-02, -1.81813779e-02, 2.82847556e-01, -9.63650606e-01,
                    -9.63654860e-01, 9.27305466e-01, -1.81746968e-02, -1.81725696e-02, -9.63652733e-01, -2.46491481e-01,
                    -2.46509097e-01, 9.99999999e-01, 2.82840875e-01, 2.82854237e-01, 9.27305467e-01],
                   [1.00000000e+00, 7.46500290e-01, -4.81827071e-01, -4.81825663e-01, 2.17152444e-01, -3.63421422e-02,
                    -3.63523906e-02, -9.27305468e-01, -4.81828929e-01, -4.81823805e-01, -3.63472666e-02, 7.46502149e-01,
                    7.46498432e-01, 1.00000000e+00, 2.17155709e-01, 2.17149178e-01, -9.27305468e-01],
                   [1.00000000e+00, -5.00000000e-01, -5.00000000e-01, -5.00000000e-01, -5.00000000e-01, 1.00000000e+00,
                    1.00000000e+00, 9.99999999e-01, -5.00000046e-01, -4.99999954e-01, 1.00000000e+00, -5.00000045e-01,
                    -4.99999954e-01, 9.99999999e-01, -5.00000045e-01, -4.99999954e-01, 1.00000000e+00],
                   [1.00000000e+00, -5.00000001e-01, -5.00000000e-01, -5.00000000e-01, -5.00000000e-01, 1.00000000e+00,
                    1.00000000e+00, 1.00000000e+00, 5.00000046e-01, 4.99999954e-01, -1.00000000e+00, 5.00000046e-01,
                    4.99999954e-01, -1.00000000e+00, 5.00000047e-01, 4.99999955e-01, -1.00000000e+00],
                   [1.00000000e+00, 1.00000000e+00, 9.99999998e-01, 9.99999998e-01, 9.99999998e-01, 9.99999998e-01,
                    9.99999998e-01, 9.99999998e-01, 9.99999999e-01, 9.99999999e-01, 9.99999999e-01, 9.99999997e-01,
                    9.99999997e-01, 9.99999997e-01, 9.99999999e-01, 9.99999999e-01, 9.99999999e-01],
                   [1.00000001e+00, -3.28530009e-01, -3.35720472e-01, -3.35711073e-01, 9.99961554e-01, -3.28577961e-01,
                    -3.28558959e-01, -3.42863086e-01, -3.35711023e-01, -3.35720524e-01, -3.28568461e-01,
                    -3.28539458e-01, -3.28520558e-01, 1.00000000e+00, 9.99961504e-01, 9.99961606e-01, -3.42863086e-01],
                   [1.00000000e+00, -5.00000002e-01, 5.00007124e-01, 4.99992877e-01, -5.00000001e-01, 7.10397300e-06,
                    -7.10383065e-06, -1.00000000e+00, -5.00003553e-01, -4.99996449e-01, -2.45075033e-11, 5.00010676e-01,
                    4.99989325e-01, -1.00000000e+00, 4.99996430e-01, 5.00003573e-01, 1.00000000e+00],
                   [1.00000000e+00, 8.28530011e-01, -1.64286653e-01, -1.64281807e-01, -4.99961550e-01, -6.71429146e-01,
                    -6.71433941e-01, 3.42863083e-01, -1.64285428e-01, -1.64283031e-01, -6.71431543e-01, 8.28528785e-01,
                    8.28531234e-01, 1.00000000e+00, -4.99957928e-01, -4.99965171e-01, 3.42863084e-01]]
        wf_soevs_a = [0.99999999, 0.99999999, 0.99999999, 0.99999999, 0.99999999, 0.99999999, 0.99999999, 0.99999999,
                      -0.99999999, -0.99999999, -0.99999999, -0.99999999, -0.99999999, -0.99999999, -0.99999999,
                      -0.99999999, -0.99999999]
        wf_soevs = [0.99999999, 0.99999999, 0.99999998, 0.99999998, 0.99999998, 0.99999998, 0.99999998, 0.99999998,
                    0.99999998, 0.99999998, 0.99999998, 0.99999998, 0.99999998, 0.99999998, 0.99999998, 0.99999998,
                    0.99999998]

        self.assertEqual(td_labels, self.wfnsym.SymLab)
        testing.assert_array_equal(td_ideal_gt, self.wfnsym.ideal_gt)
        testing.assert_array_almost_equal(soevs_a, self.wfnsym.mo_SOEVs_a)
        testing.assert_array_almost_equal(soevs_a, self.wfnsym.mo_SOEVs_b)
        testing.assert_array_almost_equal(wf_soevs_a, self.wfnsym.wf_SOEVs_a)
        testing.assert_array_almost_equal(wf_soevs_a, self.wfnsym.wf_SOEVs_b)
        testing.assert_array_almost_equal(wf_soevs, self.wfnsym.wf_SOEVs)

    def test_grim_csm(self):
        grim = [5.29207960e-08, 3.42216243e+01, 4.61543073e+01, 4.61533851e+01,
                3.11032026e+01, 4.61537384e+01, 4.61532425e+01, 2.45722518e+01,
                4.61538462e+01, 4.61538462e+01, 4.61538462e+01, 3.42218689e+01,
                3.42213798e+01, 9.65017715e-08, 3.11028027e+01, 3.11036024e+01,
                2.45722518e+01]
        csm = [1.37594074e-06, 1.37597047e-06, 1.82359058e-06, 1.82316632e-06,
               1.82340268e-06, 1.82298713e-06, 1.82383321e-06, 1.82332568e-06,
               1.59952399e-06, 1.59994741e-06, 1.59976660e-06, 2.04689851e-06,
               2.04689860e-06, 2.04686917e-06, 1.60018249e-06, 1.59933623e-06,
               1.59968333e-06]
        testing.assert_array_almost_equal(grim, self.wfnsym.grim_coef)
        testing.assert_array_almost_equal(csm, self.wfnsym.csm_coef)

    def test_symmetry_irreducible_representation_analysis(self):
        td_ir_labels = ['A1', 'A2', 'E', 'T1', 'T2']
        mo_ir_alpha = [[1.00000000e+00, 0.00000000e+00, -1.85037171e-17, 0.00000000e+00, 0.00000000e+00],
                       [9.99999993e-01, 2.77555756e-17, 3.70074342e-17, 8.85402862e-15, -8.32667268e-17],
                       [1.11774280e-10, -6.70645437e-11, -1.78838055e-10, -6.70643124e-11, 9.99999999e-01],
                       [-6.65773917e-12, 3.99479524e-12, 1.06529230e-11, 3.99510980e-12, 1.00000000e+00],
                       [-1.05116328e-10, 6.30699335e-11, 1.68186650e-10, 6.30706459e-11, 1.00000000e+00],
                       [1.00000000e+00, 1.20274161e-16, 3.70074342e-17, 9.27175003e-13, 3.63598041e-15],
                       [-1.80008876e-10, 1.08007082e-10, 2.88425191e-10, 1.09825697e-10, 9.99999999e-01],
                       [1.10892046e-10, -6.65352310e-11, -1.74195084e-10, -6.60305977e-11, 1.00000000e+00],
                       [6.91217939e-11, -4.14717450e-11, -1.07764196e-10, -4.07797476e-11, 1.00000000e+00],
                       [9.99999998e-01, -7.86407976e-17, 1.44699068e-14, 1.32152608e-10, 7.51489149e-12],
                       [-3.90762145e-11, 2.34456621e-11, 4.86761437e-10, 3.33620631e-11, 9.99999999e-01],
                       [-3.60267889e-11, 2.17547794e-11, 4.72100923e-10, 3.23546632e-11, 9.99999999e-01],
                       [8.25094868e-11, -4.52003495e-11, -1.10311713e-10, -6.45207932e-12, 1.00000000e+00],
                       [4.06625289e-11, -2.43975395e-11, 1.27392763e-10, -2.43412512e-11, 1.00000000e+00],
                       [2.00684469e-11, -1.20279157e-11, 1.27645172e-10, -1.19443899e-11, 1.00000000e+00],
                       [-6.06144024e-11, 3.64255108e-11, 1.29666426e-10, 3.66194297e-11, 1.00000000e+00],
                       [2.06038890e-14, 9.25185854e-18, 1.00000000e+00, -2.22044605e-16, 6.04079009e-10],
                       [2.31296463e-16, 6.47630098e-17, 1.00000000e+00, -6.38378239e-16, 6.04212985e-10],
                       [9.99999999e-01, 6.47630098e-17, 3.34917279e-14, 1.32623376e-09, 5.10064213e-13],
                       [-2.61686621e-11, 1.57426687e-11, 6.48272658e-10, 2.34245186e-10, 1.00000001e+00],
                       [-3.99331401e-11, 2.39592512e-11, 7.48321294e-10, 1.87253574e-10, 1.00000000e+00],
                       [6.62223239e-11, -3.97020009e-11, -2.75613513e-11, 5.54412460e-10, 1.00000000e+00]]
        wf_ir_a = [-5.64363371e-16, 9.99999991e-01, 3.60822483e-14, 5.82117687e-13, 1.67732268e-09]
        wf_ir_b = [-5.64363371e-16, 9.99999991e-01, 3.60822483e-14, 5.82117687e-13, 1.67732268e-09]
        wf_ir = [9.99999983e-01, -1.00845258e-15, 7.22570152e-14, 3.35464508e-09, 1.16442966e-12]

        self.assertEqual(td_ir_labels, self.wfnsym.IRLab)
        testing.assert_array_almost_equal(mo_ir_alpha, self.wfnsym.mo_IRd_a)
        testing.assert_array_almost_equal(mo_ir_alpha, self.wfnsym.mo_IRd_b)
        testing.assert_array_almost_equal(wf_ir_a, self.wfnsym.wf_IRd_a)
        testing.assert_array_almost_equal(wf_ir_b, self.wfnsym.wf_IRd_b)
        testing.assert_array_almost_equal(wf_ir, self.wfnsym.wf_IRd)

    def test_symmetry_matrix(self):

        symmetry_matrix = [[[1.00000000e+00, 0.00000000e+00, 0.00000000e+00],
                            [0.00000000e+00, 1.00000000e+00, 0.00000000e+00],
                            [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]],

                           [[-5.00000000e-01, 8.66025404e-01, 0.00000000e+00],
                            [-8.66025404e-01, -5.00000000e-01, 0.00000000e+00],
                            [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]],

                           [[-1.66646603e-01, 2.88686718e-01, 9.42809041e-01],
                            [8.66036987e-01, 4.99979936e-01, -1.63823853e-05],
                            [-4.71390334e-01, 8.16504771e-01, -3.33333334e-01]],

                           [[-1.66686730e-01, -8.66013819e-01, -4.71418708e-01],
                            [-2.88663551e-01, 5.00020064e-01, -8.16488390e-01],
                            [9.42809041e-01, -1.63815092e-05, -3.33333334e-01]],

                           [[8.33333333e-01, -2.88698302e-01, -4.71390333e-01],
                            [2.88651967e-01, -5.00000000e-01, 8.16504772e-01],
                            [-4.71418707e-01, -8.16488390e-01, -3.33333334e-01]],

                           [[-6.66646603e-01, 5.77361852e-01, -4.71418708e-01],
                            [5.77361852e-01, -2.00641754e-05, -8.16488390e-01],
                            [-4.71418708e-01, -8.16488390e-01, -3.33333333e-01]],

                           [[-6.66686730e-01, -5.77338685e-01, -4.71390334e-01],
                            [-5.77338685e-01, 2.00632363e-05, 8.16504772e-01],
                            [-4.71390334e-01, 8.16504772e-01, -3.33333333e-01]],

                           [[3.33333333e-01, -2.31675719e-05, 9.42809042e-01],
                            [-2.31675719e-05, -1.00000000e+00, -1.63819472e-05],
                            [9.42809042e-01, -1.63819472e-05, -3.33333333e-01]],

                           [[-1.66676699e-01, 2.88669343e-01, 9.42809041e-01],
                            [-8.66031196e-01, -4.99989968e-01, -1.63818377e-05],
                            [-4.71390333e-01, 8.16504772e-01, -3.33333334e-01]],

                           [[-1.66656635e-01, 8.66019612e-01, -4.71418708e-01],
                            [-2.88680927e-01, -5.00010032e-01, -8.16488390e-01],
                            [9.42809041e-01, -1.63820567e-05, -3.33333334e-01]],

                           [[-6.66666666e-01, 5.77361853e-01, -4.71390334e-01],
                            [-5.77338686e-01, -2.01276085e-10, 8.16504772e-01],
                            [-4.71418708e-01, -8.16488390e-01, -3.33333334e-01]],

                           [[-4.99969904e-01, 8.66042779e-01, -0.00000000e+00],
                            [8.66042779e-01, 4.99969904e-01, 0.00000000e+00],
                            [-0.00000000e+00, 0.00000000e+00, 1.00000000e+00]],

                           [[-5.00030095e-01, -8.66008028e-01, 0.00000000e+00],
                            [-8.66008028e-01, 5.00030095e-01, 0.00000000e+00],
                            [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]],

                           [[9.99999999e-01, -3.47513579e-05, 0.00000000e+00],
                            [-3.47513579e-05, -9.99999999e-01, 0.00000000e+00],
                            [0.00000000e+00, 0.00000000e+00, 1.00000000e+00]],

                           [[8.33323302e-01, -2.88680926e-01, -4.71418708e-01],
                            [-2.88680926e-01, 5.00010033e-01, -8.16488390e-01],
                            [-4.71418708e-01, -8.16488390e-01, -3.33333334e-01]],

                           [[8.33343365e-01, 2.88669342e-01, -4.71390333e-01],
                            [2.88669342e-01, 4.99989969e-01, 8.16504771e-01],
                            [-4.71390333e-01, 8.16504771e-01, -3.33333334e-01]],

                           [[3.33333335e-01, 1.15837860e-05, 9.42809041e-01],
                            [1.15837860e-05, 1.00000000e+00, -1.63819472e-05],
                            [9.42809041e-01, -1.63819472e-05, -3.33333334e-01]]]
        testing.assert_array_almost_equal(symmetry_matrix, self.wfnsym.SymMat)
