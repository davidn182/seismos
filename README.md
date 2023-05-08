# seismos

Seismos is a Python package currently under development for the inversion of hypocenters and moment tensors, and the quality control of passive seismic data. It aims to provide a range of tools for efficient and accurate analysis of seismic data, leveraging the power of the ObsPy and Pyrocko libraries.

---
# Installation

First, clone the seismos repository:

```bash
git clone https://github.com/davidn182/seismos.git
```

You can install seismos using either Poetry or pip. Both methods are described below.

## Installation with Poetry

### Create a Virtual Environment

To create a Virtual Environment and install `seismos`, we will use the `poetry install` command:

```
poetry install
```

### Activating the virtual environment[](https://python-poetry.org/docs/basic-usage/#activating-the-virtual-environment)

```
poetry shell
```

To deactivate the virtual environment and exit this new shell type 
```
exit
``` 

To deactivate the virtual environment without leaving the shell use `deactivate`.

## Installation with pip

### Create a Virtual Environment

You can create a virtual environment using the built-in `venv` module:

```bash
python -m venv myenv
```
Replace myenv with the name of the directory where you want to create the virtual environment.

Activate the virtual environment
For Linux and macOS:

```bash
source myenv/bin/activate
```

Install seismos
To install seismos using pip, run:

```bash
pip install .
```

Make sure you are in the directory containing the pyproject.toml file.

To deactivate the virtual environment, simply run:

```bash
deactivate
```

## Additional dependency: fomosto installation

f you need to create Green function databases using fomosto, you need to install it. To do this, simply run the provided `install-fomosto.sh` script:

```bash
chmod +x install-fomosto.sh
./install-fomosto.sh
```

