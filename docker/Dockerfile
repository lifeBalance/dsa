FROM python:slim-bullseye

# Install system dependencies (by default uses root user)
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive \
    apt-get install --no-install-recommends --assume-yes \
        apt-utils \
        nodejs \
        build-essential python3-dev libcairo2-dev libpango1.0-dev ffmpeg \
        dvisvgm texlive texlive-latex-extra

# Set USER_HOST, in compose.yml or from command line using --args
ARG USER_HOST=$USER_HOST
ARG UID_HOST=$UID_HOST
ARG GID_HOST=$UID_HOST

# Create a non-root user with the same name as the host user.
RUN groupadd -g "${GID_HOST}" "${USER_HOST}" \
    && useradd --create-home --no-log-init \
    -u "${UID_HOST}" -g "${GID_HOST}" "${USER_HOST}"

# Switch to the non-root user.
USER $USER_HOST

# Add the user's local bin directory to the PATH (for the user above).
ENV PATH="/home/${USER_HOST}/.local/bin:${PATH}"

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install --user jupyterlab jupyter-book theme-darcula nb-js-diagrammers jupyterlab_myst ipywidgets
RUN pip install --user manim

# Set the working directory.
WORKDIR "/home/${USER_HOST}"

CMD ["jupyter-lab","--ip=0.0.0.0","--no-browser","--allow-root"]