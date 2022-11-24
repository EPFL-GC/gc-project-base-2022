# Python Dependencies
To get started, create the `make_it_stand` conda environment using the `environment.yml` file:
```
conda env create -f environment.yml
```

### `libigl`
On M1 Macs, `libigl` has to be compiled from source:
```
git clone git@github.com:libigl/libigl-python-bindings.git
cd libigl-python-bindings
python setup.py develop
```