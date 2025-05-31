# Process Visualizer

This script visualizes the **number of processes per user** from a JSON input file using a bar chart.

---

## ✅ Prerequisites

- Python 3
- [`matplotlib`](https://matplotlib.org/) library

You can install `matplotlib` with:

```
pip install matplotlib
```

## JSON Input Format
The script expects a list of process objects in the following format:
```
[
  {
    "Id": 2112,
    "Name": "svchost",
    "CPU": 18.45,
    "Mem": 20.68,
    "User": "NT AUTHORITY\\SYSTEM"
  },
  {
    "Id": 3928,
    "Name": "vdagent",
    "CPU": 17.97,
    "Mem": 11.23,
    "User": "NT AUTHORITY\\SYSTEM"
  }
]
```

## 
```
python json-visualizer.py processes.json
```