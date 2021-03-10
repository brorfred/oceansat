
import numpy as np

import pytest
import oceansat


def test_laws_2000_scalar():
    eprod = oceansat.export_production.laws_2000(pprod=100, sst=15)
    assert eprod > 100/100
    assert eprod <= 100
    assert eprod == pytest.approx(30.78, 0.1)

def test_laws_2000_array():
    pprod = np.full([100,100], 100)
    sst = np.full([100,100], 15)
    eprod = oceansat.export_production.laws_2000(pprod=pprod, sst=sst)
    assert eprod == pytest.approx(30.78, 0.1)

def test_laws_2011a():
    eprod = oceansat.export_production.laws_2011a(pprod=100, sst=15)
    assert eprod > 100/100
    assert eprod <= 100
    assert eprod == pytest.approx(22.30, 0.1)

def test_dunne_2005():
    eprod = oceansat.eprod(pprod=100, sst=15, z_eup=50)
    assert eprod == pytest.approx(30.78, 0.1)

def test_eprod():
    eprod1 = oceansat.eprod(pprod=100, sst=15, z_eup=50)
    eprod2 = oceansato.export_production.dunne_2005(pprod=100, sst=15,z_eup=50)
    assert eprod1 == eprod2
    assert eprod2 == pytest.approx(30.78, 0.1)
    eprod = oceansat.export_production.dunne_2005(pprod=100, sst=15,z_eup=30, chl=10)
    assert eprod == pytest.approx(23.11, 0.1)
