# Source code
The source code is broken into two parts: the master Web server, and the subscriber workers. A subscriber is a Docker container which will be attached to a GPU compute instance. One Docker container represents one CCTV.

Due to the size of the Docker container (~21GB), it will not be hosted on GitHub. Everything here belongs to the master Web server. Please go to https://dord.mynetgear.com/container.tar to download the subscriber Docker container.
