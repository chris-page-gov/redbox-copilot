# Workers and Queues

The Worker is a set of service that runs in the background and perform tasks that are too resource-intensive to run on the Core API. This worker includes:

- Ingesting files
- Embedding chunks of text

The Workers are designed to be horizontally scalable. This means that we can add more instances of the Workers to handle more load. The Workers are also designed to be resilient. This means that if one instance of the Worker fails, another instance can take over.

![Document Processing Pipeline](../assets/document_processing_pipeline.png)

## Scaling

When running locally in docker compose, there is only one replica of each Worker. When running in the cloud, we can scale the number of replicas up or down depending on the load. For AWS this will be based on the number of messages in the SQS Queue. For local development, we can scale the number of replicas up or down manually by adding the `replicas` key to the `docker-compose.yml` file for each service.

## FastStream

We are using [FastStream](https://faststream.airt.ai/latest/faststream/) to handle our streaming between Microservices. It handles the connection to Redis (and other Queues) with a high-performance Python client based on FastAPI and Pydantic. It has support for multiple brokers, automatic documentation, and tests. 

## Worker

The Worker is responsible for:
* ingesting files into the system. The Ingester Worker reads a [`File`](../code_reference/models/file.md) reference from its queue and then reads the file from the Object Store. The Worker then processes the file and stores the file in the Database. The worker also sends created [`Chunk`](../code_reference/models/chunk.md) references to the Worker via the `embedding-queue`.
* embedding chunks of text. The Embedder Worker reads a [`Chunk`](../code_reference/models/chunk.md) reference from its queue and then reads the text from the Database. The Worker then embeds the text with it instance of the embedding model. The worker then stores the embedding in the Database.
