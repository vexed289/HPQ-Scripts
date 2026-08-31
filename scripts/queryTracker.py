from datetime import datetime
import json
from pathlib import Path
import matplotlib.pyplot as plt

def snapshot(data):
    fname = Path(__file__).name
    date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"snapshots/{fname} - {date}.json"

    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

def snapshotFigure(fname, fig, ax):
    date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"figures/{fname} - {date}"
    
    plt.savefig(filename)