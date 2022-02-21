#### Review of Amazon DynamoDB

#### Finding a needle in a haystack

Data without a schema is useless. You get a document from MongoDB, what do you do with it? Read some fields? You need to know the names, types and meanings of those fields. That's a schema.
When people say that MongoDB “has no schema”, they really mean that it does not enforce schema the way SQL databases do. MongoDB pushes schema concerns up to your application level, where you can handle them more flexibly. For example, in order to add a new field to your documents, you don't need to do an all-or-nothing ALTER on your collection—potentially millions of entries. You just add that field to your ODM (Mongoose) schema and you're done.

----

Not entirely true. There are realtime apps that can rely on fields created on the fly. Adding a field to Mongoose model means a new deploy process. There are ODMs that doesn't require a fixed schema definition, Mongorito for instance.

----

If get the whole data in spark frequently or update frequently, Cassandra will be dead.
So many limitations on CQL.
If you are using python, the only one choice of driver is DataStax one. You cannot set the host ports of Cassandra servers if you use the ORM model.
Now, I'm moving the dataset to mongoDB. I think they are much useful than Cassandra. At least, I can search one single item fast.

----

#### A Comprehensive Comparative Analysis of NoSQL Engines

List of NoSQL database engines:
* Solr/Elastic Search
* MongoDB Atlas (does not enforce schemas. bad for management. MongoDB is terrible because of the Mongoose ORM (yes! an ORM over NoSQL). [Run anywhere in the world with Atlas. Deploy your data in over 80 regions on AWS, Azure, and Google Cloud – including simultaneously with multi-cloud clusters.]
https://stackoverflow.com/questions/13107976/why-does-mongoose-use-schema-when-mongodbs-benefit-is-supposed-to-be-that-its)
* Redis

#### Cassandra
Cassandra was modelled upon DynamoDB - they are mostly the same. DynamoDB and Cassandra both belong to key-value stores, a category of NoSQL databases. They are both (A,P) databases in CAP theory parlance - both of them have only eventual (or weak) consistency, as they sacrifies C to achieve higher A (availability). They both use the Gossip protocol for membership protocol and failure detection. They both use consistent hashing ring of nodes for  distributed hash table (DHT), which has some nuances of optimisation. NoSQL does not mean the absence of a SQL query language, it is actually the abbreviation of NoSQL. For ease of basic CRUD (create, read, update, and write) operations, the developers of both DynamoDB and Cassandra developped some variants of SQL lanuages.

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