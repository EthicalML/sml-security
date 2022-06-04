MLOps Project {{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}

## Usage

You can get started by installing the environment with the following commands.

Make sure you have all dependencies set up as outlined in the Dependencies section.

```bash
# Recommended to create new environment
make conda-env-create
conda activate {{ cookiecutter.repo_name }}

make install
```

Once you have set up you will have a `poetry.lock` file with all the dependencies for full reproducibility.

You can then run the server locally for a test with the following command:

```
make local-run
```

And then you can send a test request to your deployed ML model runtime with the following command:

```
make local-test-request
```

Finally we can just stop the mlserver process:

```
make local-stop
```

## Security

We can perform relevant security checks for the package by using the commands that we have available.

In order to run the python-specific commands we need to make sure to set up the environment accordingly.

```bash
# Recommended to create new environment
make conda-env-create
conda activate {{ cookiecutter.repo_name }}-dev

make install-dev
```

Now we can run some of the base security checks:

```bash
# Check CVEs in any of the dependencies installed
make security-local-dependencies 

# Check for insecure code paths
make security-local-code

# Check for old dependencies
make security-local-dependencies-old 
```

In order to perform the container security scans, it is a pre-requisite to have built the image as below.

```
make docker-build
```

Now we can run the dependency scans on top of these.

```
make security-docker
```

## Dependencies

We recommend using the [version manager asdf-vm](https://github.com/asdf-vm/asdf) for simpler installation of all required command-line dependencies used in this project for development, testing, security, etc.

Once you have set up corretly asdf-vm, you can install all relevant dependencies by running the following:

```
make install-dev-deps
```

In order to install the package you will need to use the [Poetry dependency manager](https://github.com/python-poetry/poetry).



## Project Organization

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://github.com/EthicalML/sml-security">secure production machine learning cookiecutter</a>. #cookiecutterdatascience</small></p>
