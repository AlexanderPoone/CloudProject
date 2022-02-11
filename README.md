# Cloud Computing Project
**DRAFT**

## Group members

## Objective
Modern cloud computing applications are usually architected as distributed collections of loosely coupled microservices, with each collection of microservices performing some business logic.

We are going to build a microservice pipeline. The pipeline is similar to a DAG (directed acyclic of graph), like Apache Airflow or Kafka.

Amazon EC2 instances are created on demand using the Boto3 library, depending on the input data size.

## GPU Instances
Amazon EC2 P3 Instances have up to 8 NVIDIA Tesla V100 GPUs.
Amazon EC2 P4 Instances have up to 8 NVIDIA Tesla A100 GPUs.
Amazon EC2 G3 Instances have up to 4 NVIDIA Tesla M60 GPUs.
Amazon EC2 G4 Instances have up to 4 NVIDIA T4 GPUs.
Amazon EC2 G5 Instances have up to 8 NVIDIA A10G GPUs.
Amazon EC2 G5g Instances have Arm-based AWS Graviton2 processors.
