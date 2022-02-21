#### Review of *Classification of Big Point Cloud Data Using Cloud Computing (Liu, Boehm 2015)*

![project_pipeline.png](project_pipeline.png)

GPU instance Visio

Google Colaboratory (Colab) lacks integration with anything other than Google Drive and Google Cloud platform, hard limit on hard disk, GPU VRAM and RAM. Storage is not always on SSD.

discovery.ucl.ac.uk

[Classification of big point cloud data using cloud computing](https://discovery.ucl.ac.uk/id/eprint/1471584/1/isprsarchives-XL-3-W3-553-2015.pdf)

Kun Liu, Jan Boehm

ISPRS-International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences 40, 553-557, 2015

Point cloud data plays an significant role in various geospatial applications as it conveys plentiful information which can be used for different types of analysis. Semantic analysis, which is an important one of them, aims to label points as different categories. In machine learning, the problem is called classification. In addition, processing point data is becoming more and more challenging due to the growing data volume. In this paper, we address point data classification in a big data context. The popular cluster computing framework Apache Spark is used through the experiments and the promising results suggests a great potential of Apache Spark for large-scale point data processing.

-------------------------------------------------------------

#### IoT Example
Nadir cameras (RGB or LiDAR) like the image below [Fairbanks_Circle.png]. Smart City lampposts. Scale out G5 GPU EC2 instances. Stream of images. May need ZeroMQ or MQTT installed in the master node to ensure the fairness of each camera...

[project_pipeline2.png]

-------------------------------------------------------------
Training new models is faster on a GPU instance than a CPU instance. You can scale sub-linearly when you have multi-GPU instances or if you use distributed training across many instances with GPUs.

The AWS Deep Learning AMI (DLAMI) comes preconfigured with NVIDIA CUDA and NVIDIA cuDNN, as well as the latest releases of the most popular deep learning frameworks.
* Amazon EC2 P3 Instances have up to 8 NVIDIA Tesla V100 GPUs.
* Amazon EC2 P4 Instances have up to 8 NVIDIA Tesla A100 GPUs.
* Amazon EC2 G3 Instances have up to 4 NVIDIA Tesla M60 GPUs.
* Amazon EC2 G4 Instances have up to 4 NVIDIA T4 GPUs.
* Amazon EC2 G5 Instances have up to 8 NVIDIA A10G GPUs.
* Amazon EC2 G5g Instances have Arm-based AWS Graviton2 processors.

#### Computer graphics processing pipeline in the cloud using EC2 and Apache Airflow

Adding a CCTV is embarassingly parallel.

Compare to Amazon Lambda, a serverless service offered by AWS. It is very hard if not possible to execute external programs. EC2 is easier to do this. 3 sample programs lastiles.exe, lasground.exe, and lasmerge.exe
and do benchmark using Python time.time(), compare to lasground on a single instance.

WebSocket for communication

#### Preamble
We can programmatically create EC2 instances using the Boto3 library. Commands can be issued programmatically using the paramiko library, which is basically a SSH (Secure Shell) wrapper.
Apache Airflow is a local program. Its use is to orchestrate the EC2 instances. Specifically, we define an Airflow task as some SSH commands to the EC2 instances. Those Airflow tasks are linked together by a direct acyclic graph (DAG).

lasground as an example

Computer graphics include bitmap images, vector images, 3D meshes, and 3D point clouds.

#### Rationale for Using Cloud Computing
Besides cloud storage, cloud computing is particularly useful for deep learning. Procedures in the pipeline, including smoothing, baking and rendering, are resource-hungry and time-consuming process.

Many reasons: 
(Multitenancy) There may be multiple users that upload their CG files for processing.

users do not need to install software since the web browser can access it, allows multiple concurrent users without degrading performance too much, users do not need to have actual access to expensive hardware, allows sharing and collaboration, good for logging etc. High availability, scale with resources. As with any cloud pipelines, it is also good for commercialisation, you can accept multiple payment methods.
Sharing and. Archive and store results are done more easily: Traffic cameras from CCTVs. You know, the backgrounds of CCTV frames are nearly identical, the cloud can deduplicate the images to save space. It's easier to add more CCTVs on the cloud. Shared deduplication database.

Without the cloud, it is very difficult to scale when the number of CCTV increases. Task queues like Celery does not provide more or improve hardware, and therefore scale poorly.

Scale out on demand: it is quite parallel

Scale up on demand: VRAM is crucial in deep learning, OOM (out-of-memory) error. the clouds orchestrator can give more VRAM to nodes

Duplicate EBS:

#### Example 1: Image Detection on CCTV Frames for Traffic Analysis
Ubuntu Visio!!!
This is a stream
Easy to scale, deploy more instances

As the number of CCTVs increases, the number of repeated pixel sequence sharply increases. We can use run-length encoding and LZ77.

-----------
Divide and conquer is good
#### Example 2: Point Cloud Classification Server
In fact, the open data Point Cloud from CEDD for the entire Hong Kong is 100TB large. 0.5 km^2 tiles

Sort the point cloud by coordinates so that it can be split into tiles. It can be parallelized using merge sort for MapReduce in Hadoop or Spark.

Tile and distribute to all
Each node perform classfications
merge results (can be recursive!)

Ubuntu Visio!!!

#### Master/worker Model

Duplicate EBS that contains scripts and software like Blender, CompareCloud, Maya and MeshLab. We can manipulate the abovementioned software using their scripting capabilities. We do not need graphical interface to use these software, since it supports languages like MEL and Python.

Visio!!!!!!!!

Merge models on the master node.

We can define at least 10 nanoservices

Nanoservice models. Similar nanoservices
How about class inheritance in nanoservices?

Kubeflow. Kubenetes is good for very large projects, but there are too many components. Besides, the person needs to have an in-depth knowledge of technologies like Docker, remote procedure call and YAML configuration files. It has a very steep learning curve.

A nanoservice is just a function. It can have a output value that pass to the next nanoservice in the pipeline, or a execution result code either to indicate the operation is successful, or the error type for the pipeline to do corresponding actions if unsuccessful.

Apache Airflow, is an orchestration service AirBNB. It has a hard restriction that the workflow be a direct acyclic graph, therefore no cycles is allowed. Comparing DAG to a generic graph, sometimes we need to execute a nanoservices multiple times, but disallowing loops is actually a good design. It avoids stuck in an infinite loop (e.g. deadlocks caused by waiting of resources, or programming faults). Besides, it makes the flow more readable and understandable as it avoid clumping (less edges).

Comparing DAG to the traditional sequential pipeline, a DAG allows sharing of nodes (multiple edges pointing towards or emanating from a common microservice), enhancing the reusability.

Apache Storm

Break down into nanoservices:
1. Determine and allocate on-demand computing resources by the input dataset size
2. Break down (tile) the dataset if it is too large

The same applies to point cloud, images, etc
