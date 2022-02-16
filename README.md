# Cloud Computing Project
**DRAFT**

<!--## Group members-->

## Objective
We are writing a lightweight cloud storage deduplication program. Issues scalability, deduplication granularity and usefulness, and security will be addressed.

DynamoDB is used to store the key-value pairs of <block id; binary content>, <file id; user id, file path, file sequence, metadata>, <user id; metadata> 

The front end is planned to be written in Qt (or Flutter), so that it can be used on mobile devices.

Amazon EC2 instances are created on demand using the Boto3 library, depending on the input data size.

## 0. Ideas
Deduplication is a trade-off between user's storage size and file reassembly time.
Points to consider:
* What the optimal block size is (a.k.a. granularity)
* How much latency is needed to reassemble the files
* How to store the blocks in the database without security implications
### a. On-demand deduplication
Elasticity in Cloud Computing. Deduplicate when the user's storage is nearly full, exchange for longer reassembly time. In another scenario: small local cloud storage providers that do not have large data centres. They can save the cost to buy new hardware.
### b. Distributed Data Deduplication

## 1. Algorithms
a. Rabin fingerprinting
b. AES

## 2. Case Studies
* Dropbox Security Breach due to loophole in Deduplication algorithm:

* [https://github.com/driverdan/dropship](https://github.com/driverdan/dropship)
* [https://blog.fosketts.net/2011/07/11/dropbox-data-format-deduplication/](https://blog.fosketts.net/2011/07/11/dropbox-data-format-deduplication/)
* [https://news.ycombinator.com/item?id=2478567](https://news.ycombinator.com/item?id=2478567)
The algorithm must be designed with special care to avoid birthday attacks:
https://en.wikipedia.org/wiki/Birthday_attack

* StorReduce on Amazon

## References

<!-- Grid computing: needs to stop other instances once the solution is found. -->
