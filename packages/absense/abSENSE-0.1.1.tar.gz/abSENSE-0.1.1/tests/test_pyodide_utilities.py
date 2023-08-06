from abSENSE import pyodide_utilities
import pytest


def test_get_plots_from_text():
    data = (
        'Species\tDistance\tNP_010181.2\tNP_009362.1\tNP_014555.1\tNP_116682.3\tNP_011284.1\tNP_011878.1\tNP_013320.1\tNP_014160.2\tNP_014890.1\n'
        'S_cer|0|2284|1027|712|352|308|588|1491|941|394\n'
        'S_par,0.051,2254,1016,698,171,225,522,1205,927,264\n'
        'S_mik,0.088,2234,1018,696,92.8,179,446,1013,889,254\n'
        'S_kud,0.104,2197,1010,688,82,178,455,996,893,271\n'
        'S_bay,0.108,2200,1008,684,0,191,439,910,885,230\n'
        'S_cas,0.363,1895,909,N/A,0,0,0,141,638,58.9\n'
        'K_wal,0.494,1767,903,617,0,0,0,101,0,0\n'
        'A_gos,0.518,1736,875,N/A,0,0,0,63.2,657,0\n'
        'K_lac,0.557,1691,894,611,0,0,0,102,0,0\n'
        'A_nid,0.903,1099,691,N/A,0,0,0,0,378,0\n'
        'S_pom,0.922,1194,684,344,0,0,0,0,0,0\n'
        'Y_lip,0.954,1297,714,N/A,0,0,0,0,375,0'
    )

    with pytest.warns(UserWarning):
        for plot in pyodide_utilities.get_plots_from_text(data, 0.002, 400, 9_000_000):
            plot.show()
            break
    assert 0
