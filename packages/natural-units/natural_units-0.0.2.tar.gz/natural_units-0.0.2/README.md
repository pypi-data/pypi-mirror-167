# natural_units

Wrapper for various units:

| Unit      | Description | Notes | 
| ----------- | ----------- | ------------ | 
| base      | general        | super class | 
| si        | m, kg, s, A, K, mol, cd       |
| hep   | $c=\hbar=\epsilon_0=k_B=1$         | checks mass dimension compatibility | 
| plain_hep       | $c=\hbar=\epsilon_0=k_B=1$         | like natural, but without mass dimension checks |
| geometrized | $c=G=1$ | checks length dimension compatibility |
| planck | $c=\hbar=G=k_B=1$ | |
| stoney | $c=G=k_e=e=1$ | |
| hartree_atomic | $e=m_e=\hbar=k_e=1$ | |
| particle_atomic | $c=m_e=\hbar=\epsilon_0=1$ | |
| qcd | $c = m_p=\hbar=\epsilon_0 = 1$ | |
