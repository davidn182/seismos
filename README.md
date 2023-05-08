# seismos

Seismos is a Python package currently under development for the inversion of hypocenters and moment tensors, and the quality control of passive seismic data. It aims to provide a range of tools for efficient and accurate analysis of seismic data, leveraging the power of the ObsPy and Pyrocko libraries.

## Create a Virtual Environment

To create a Virtual Environment and install `seismos`, we will use the `poetry install` command:

```
poetry install
```

## Activating the virtual environment[](https://python-poetry.org/docs/basic-usage/#activating-the-virtual-environment)

```
poetry shell
```

To deactivate the virtual environment and exit this new shell type 
```
exit
``` 

To deactivate the virtual environment without leaving the shell use `deactivate`.

## Additional dependency: fomosto installation

f you need to create Green function databases using fomosto, you need to install it. To do this, simply run the provided `install-fomosto.sh` script:

```bash
chmod +x install-fomosto.sh
./install-fomosto.sh
```

