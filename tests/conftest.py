from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from agcounts.extract import get_counts

data_path = Path("./data")
raw_data_path = data_path / "raw"
cp_data_path = data_path / "CentrePointCounts"
al_data_path = data_path / "ActiLifeCounts"


@pytest.fixture
def agcounts_serial(request):
    epoch, freq = request.param
    signals = pd.read_csv(
        raw_data_path / f"raw_{epoch}_{freq}.csv", skiprows=0, header=None
    )
    counts = get_counts(np.array(signals), freq=freq, epoch=epoch, fast=False)
    return counts


@pytest.fixture
def agcounts(request):
    epoch, freq = request.param
    signals = pd.read_csv(
        raw_data_path / f"raw_{epoch}_{freq}.csv", skiprows=0, header=None
    )
    counts = get_counts(np.array(signals), freq=freq, epoch=epoch, fast=True)
    return counts


@pytest.fixture
def cp_counts(request):
    epoch, freq = request.param
    counts = pd.read_csv(
        cp_data_path / f"raw_{epoch}_{freq}_CentrePointCounts.csv", skiprows=0
    )
    counts = counts[["X (axis 2)", "Y (axis 1)", "Z (axis3)"]].to_numpy()
    return counts


@pytest.fixture
def al_counts(request):
    epoch, freq = request.param
    counts = pd.read_csv(
        al_data_path / f"raw_{epoch}_{freq}_counts{epoch}sec.csv", skiprows=10
    )
    counts = counts[["Axis2", "Axis1", "Axis3"]].to_numpy()
    return counts
