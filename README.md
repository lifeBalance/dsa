# DSA
A compilation of data structures and algorithms using [Jupyter Notebooks](https://jupyter.org/).

## About the Docker setup
I put together my own Dockerfile based on the [Python official image](https://hub.docker.com/_/python). It's worth mentioning a couple issues:

* When mounting host filesystems onto the container, we may face some permission issues if the folders are empty. Just throw a dummy file in there and you'll be fine.
* Another *funny* (it made me lose my shit tbh) thing was mounting the ``src`` not directly on top of the container's home directory, because that way, we're smashing the `~/.local/bin` where all the Jupyter stuff gets installed.
* Oh, I also added [manim](https://docs.manim.community/en/stable/index.html), because I want to try have some fun creating some videos to explain sorting algorithms (but we'll see).