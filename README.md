# Cloud Computing Project
**DRAFT**

## Group members

## Objective
Modern cloud computing applications are usually architected as distributed collections of loosely coupled microservices, with each collection of microservices performing some business logic.

We are going to build a microservice pipeline. The pipeline is similar to a DAG (directed acyclic of graph), like Apache Airflow or Kafka.

Amazon EC2 instances are created on demand using the Boto3 library, depending on the input data size.