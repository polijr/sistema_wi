from django.test import TestCase

# Create your tests here.
"""Testes do algoritmo de performance

    Execute com pytest .\test_algoritomo_performance.py -v -s
"""

import pytest
from datetime import date
from algoritmo_performance import calcula_performance

def test_calcula_performance_com_atrasos():
    pedidos = [
        {
            'data_ocoren': date(2018,11,22),
            'data_conemb': date(2018,11,9),
            'prazo': 4
        },
        {
            'data_ocoren': date(2018,11,23),
            'data_conemb': date(2018,11,11),
            'prazo': 10
        },
        {
            'data_ocoren': date(2018,11,26),
            'data_conemb': date(2018,11,11),
            'prazo': 10
        }
    ]
    performance = calcula_performance(pedidos)
    print(f'| performance calculada:{performance}')
    assert performance == pytest.approx(60, abs=1)

def test_calcula_performance_com_e_sem_atrasos():
    pedidos = [
        {
            'data_ocoren': date(2018,11,22),
            'data_conemb': date(2018,11,9),
            'prazo': 4
        },
        {
            'data_ocoren': date(2018,11,23),
            'data_conemb': date(2018,11,14),
            'prazo': 10
        },
        {
            'data_ocoren': date(2018,11,30),
            'data_conemb': date(2018,11,11),
            'prazo': 10
        }
    ]
    performance = calcula_performance(pedidos)
    print(f'| performance calculada:{performance}')
    assert performance == pytest.approx(64, abs=1)

def test_performance_todas_entregas_no_dia_cem_porcento():
    pedidos = [
        {
            'data_ocoren': date(2018,11,13),
            'data_conemb': date(2018,11,9),
            'prazo': 4
        },
        {
            'data_ocoren': date(2018,11,24),
            'data_conemb': date(2018,11,14),
            'prazo': 10
        },
        {
            'data_ocoren': date(2018,11,21),
            'data_conemb': date(2018,11,11),
            'prazo': 10
        }
    ]
    performance = calcula_performance(pedidos)
    print(f'| performance calculada:{performance}')
    assert performance == 100