# DSA
A compilation of data structures and algorithms using [Jupyter Notebooks](https://jupyter.org/).

## About the Docker setup
Optionally, you can get Jupyter Lab up and running using the Docker files under the ``docker`` folder. I put together my own Dockerfile based on the [Python official image](https://hub.docker.com/_/python). It's worth mentioning a couple issues:

* When mounting host filesystems onto the container, we may face some permission issues if the folders are empty. Just throw a dummy file in there and you'll be fine.
* Another **annoying** thing was mounting the ``src`` not directly on top of the container's home directory, because that way, we're smashing the `~/.local/bin` where all the Jupyter stuff gets installed.
* Oh, I also added [manim](https://docs.manim.community/en/stable/index.html), because I want to try have some fun creating some videos to explain sorting algorithms (but we'll see).
* The [nb-js-diagrammers](https://pypi.org/project/nb-js-diagrammers/) is a cool extension that enables magics to use several JavaScript diagram generators (I'm mainly interested in Mermaid, for drawing trees).

## About the Poetry setup
Having to launch VSCode in a separate window to connect to the running container was a bit of a PITA, so I decided to put together a virtual environment using [Poetry](https://python-poetry.org). In order to do that I had to:

1. Install [pipx](https://github.com/pypa/pipx):

```
python -m install --user pipx
```

2. Install **Poetry** using pipx:

```
pipx install poetry
```

In order to launch Jupyter Lab, we have to enable the environment (from the project folder that contains the `pyproject.toml` file):

```
poetry shell
```

In order to exit this environment use ``exit``.

> Use ``poetry env info`` to see information about the virtual environment.