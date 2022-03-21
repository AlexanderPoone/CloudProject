# Source code
The source code is broken into two parts: the **master Web server**, and the **subscriber workers**. A subscriber workers is a Docker container which will be attached to a GPU compute instance. One Docker container represents one CCTV.

Due to the size of the Docker container (~21GB), it will not be hosted on GitHub. Everything here belongs to the master Web server. Please go to https://dord.mynetgear.com:14443/container.tar to download the subscriber Docker container.

## Requirements
To install the dependencies, enter the following in the command line:
```
pip3 install -r requirements.txt
```

Since GPU instances are expensive, you may test our program on Windows. Find a PC with a CUDA-compatible Nvidia GPU, install [CUDA 11.3.0+](https://developer.nvidia.com/cuda-downloads), [WSL2](https://docs.microsoft.com/en-us/windows/wsl/install), and [Docker Desktop](https://www.docker.com/products/docker-desktop/) to use our Docker container. For Linux and Mac, the procedure is generally the same.
