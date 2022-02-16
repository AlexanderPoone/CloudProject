# Cloud Computing Project
**DRAFT**

<!--## Group members-->

## Objective
We are writing a lightweight cloud storage deduplication program. Issues scalability, deduplication granularity and usefulness, and security will be addressed.

DynamoDB is used to store the key-value pairs of <block id, binary content>, <user id, filepath, file sequence, metadata>. (maybe more)

The front end is planned to be written in Qt (or Flutter), so that it can be used on mobile devices.

Amazon EC2 instances are created on demand using the Boto3 library, depending on the input data size.

## References
More to add...
* [https://github.com/driverdan/dropship](https://github.com/driverdan/dropship)

<!-- Grid computing: needs to stop other instances once the solution is found. -->
