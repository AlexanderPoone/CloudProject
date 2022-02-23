### Review of Amazon DynamoDB
#### Finding a needle in a haystack: A Comprehensive Comparative Analysis between two AWS database engines: DynamoDB and DocumentDB
Critical review

https://db-engines.com/en/system/Amazon+DynamoDB%3BMongoDB%3BRedis

Amazon Web Services (AWS) offers many types of databases on the cloud - DynamoDB, DocumentDB, MemoryDB, ElasticCache, Aurora, RedShift, among many others. Such diversity may be confusing to non-experts, considering the technologies behind DynamoDB, DocumentDB and MemoryDB - Dynamo, MongoDB and Redis, are essentially NoSQL key-value stores. In fact, their differences are numerous and these databases have divergent use cases.

| Comparison | DocumentDB (Mongo) | DynamoDB |
|---------|---------|-----------------|
| Type | NoSQL: Key-value store: document store | NoSQL: Key-value store: wide-column store |
| Relational Joins | Not supported | Not supported |
| SQL Support | None | Only partial support: PartiQL |
| ACID-compliant | Lacks Isolation | Weak (eventual) Consistency |
| CAP theory taxonomy | Focus on CA | Focus on AP |
| PACELC theory taxonomy ('else': what to focus if there is no failure) | PA/EC: In the baseline case, the system guarantees reads and writes to be consistent. | PA/EL: If a partition occurs, they give up consistency for availability, and under normal operation they give up consistency for lower latency. |

Document-oriented databases are inherently a subclass of the key-value store, another NoSQL database concept. The difference lies in the way the data is processed; in a key-value store, the data is considered to be inherently opaque to the database, whereas a document-oriented system relies on internal structure in the document in order to extract metadata that the database engine uses for further optimization. Although the difference is often negligible due to tools in the systems,[a] conceptually the document-store is designed to offer a richer experience with modern programming techniques.

| Problem | DocumentDB (Mongo) Technique | DynamoDB Technique | Advantage |
|---------|---------|-----------------|-----------|
| Dataset partitioning | | Consistent hashing | Incremental, possibly linear scalability in proportion to the number of collaborating nodes.
| Highly available writes | | Vector Clock or Dotted-Version-Vector Sets, reconciliation during reads | Version size is decoupled from update rates.
| Handling temporary failures | | Sloppy Quorums and hinted handoff | Provides high availability and durability guarantee when some of the replicas are not available.
| Recovering from permanent failures | | Anti-entropy using Merkle tree | Can be used to identify differences between replica owners and synchronize divergent replicas pro-actively.
| Membership and failure detection | | Gossip-based membership protocol and failure detection | Avoids having a centralized registry for storing membership and node liveness information, preserving symmetry.

Both Cassandra and DynamoDB uses 'hinted handoff'. What is 'sloppy quorum', 'hinted handoff' and 'anti-entropy' by the way:

- Sloppy: If you describe someone's work or activities as sloppy, you mean they have been done in a careless and lazy way.
- Quorum: Refers to Apache ZooKeeper quorum, the minimum number of servers required to run the Zookeeper is called Quorum. ZooKeeper replicates whole data tree to all the quorum servers. (https://jimdowney.net/2012/03/05/be-careful-with-sloppy-quorums/ The rule "R + W > N ensures strong consistency in a cluster" does not hold for sloppy quorums. A page in the Riak wiki states that "R + W > N ensures strong consistency in a cluster" and includes a reference to the post by Vogels on eventual consistency. However, a recent Basho posting states that Riak uses sloppy quorums by default, though it uses strict quorums whenever the values of PR and PW are used rather than R and W. Overall, I didn’t find the Riak documentation clear on this important distinction.)

- Hinted: With notice
- Handoff: the act of warding off an opposing player with the open hand

The claims by MongoDB that it fulfils all of the four ACID properties: atomicity, consistency, isolation, and durability is dubious.




Data without a schema is useless. You get a document from MongoDB, what do you do with it? Read some fields? You need to know the names, types and meanings of those fields. That's a schema.
When people say that MongoDB “has no schema”, they really mean that it does not enforce schema the way SQL databases do. MongoDB pushes schema concerns up to your application level, where you can handle them more flexibly. For example, in order to add a new field to your documents, you don't need to do an all-or-nothing ALTER on your collection—potentially millions of entries. You just add that field to your ODM (Mongoose) schema and you're done.

----

Not entirely true. There are real-time apps that can rely on fields created on the fly. Adding a field to Mongoose model means a new deploy process. There are ODMs that doesn't require a fixed schema definition, Mongorito for instance.

----

If get the whole data in spark frequently or update frequently, Cassandra will be dead.
So many limitations on CQL.
If you are using python, the only one choice of driver is DataStax one. You cannot set the host ports of Cassandra servers if you use the ORM model.
Now, I'm moving the dataset to mongoDB. I think they are much useful than Cassandra. At least, I can search one single item fast.

----

List of NoSQL database engines:
* Solr/Elastic Search
* MongoDB Atlas (does not enforce schemas. bad for management. MongoDB is terrible because of the Mongoose ORM (yes! an ORM over NoSQL). [Run anywhere in the world with Atlas. Deploy your data in over 80 regions on AWS, Azure, and Google Cloud – including simultaneously with multi-cloud clusters.]
https://stackoverflow.com/questions/13107976/why-does-mongoose-use-schema-when-mongodbs-benefit-is-supposed-to-be-that-its)
* Redis

#### Cassandra
Cassandra was modelled on DynamoDB - they are mostly the same. DynamoDB and Cassandra both belong to key-value stores, a category of NoSQL databases. They are both (A,P) databases in CAP theory parlance - both of them have only eventual (or weak) consistency, as they sacrifice C to achieve higher A (availability). They both use the Gossip protocol for membership protocol and failure detection. They both use consistent hashing ring of nodes for distributed hash table (DHT), which has some nuances of optimisation. NoSQL does not mean the absence of a SQL query language; it is actually the abbreviation of NoSQL. For ease of basic CRUD (create, read, update, and write) operations, the developers of both DynamoDB and Cassandra developed some variants of SQL languages.

Cassandra is a wide-column store like Goggle BigTable. DynamoDB is multi-model. Cassandra has write optimisation, DynamoDB is more suitable for large reads.

Cassandra and MongoDB are very different
Cassandra: strict restriction on data types. MongoDB: Since CSON collections are JSON files in essential, there are no restriction on data types. They are dynamic as in a document NoSQL database.

Nested tuples/UDTs in Cassandra

#### CQL for Cassandra Vs. PartialQL for DynamoDB
As the name of PartialQL implies, it is 'partial' SQL, many feature from a 'full-fledged' SQL language is absent. Both does not support relational joins, because the databases are not relational databases; they are key-value stores after all.

#### DynamoDB
Partition key
The partition key is part of the table's primary key. It is a hash value that is used to retrieve items from your table and allocate data across hosts for scalability and availability.
Sort key - optional
You can use a sort key as the second part of a table's primary key. The sort key allows you to sort or search among all items sharing the same partition key.

----

In Amazon DynamoDB, you can use either the DynamoDB API, or PartiQL, a SQL-compatible query language, to query an item from a table.
With PartiQL, you can perform a query by using the ExecuteStatement action and the Select statement on the partition key.

SELECT AlbumTitle, Year, Price
FROM Music
WHERE Artist='No One You Know' 
Using the SELECT statement in this way returns all the songs associated with this particular Artist.
