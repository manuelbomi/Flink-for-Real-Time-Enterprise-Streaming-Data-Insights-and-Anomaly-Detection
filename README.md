# Flink for Real-Time Enterprise Streaming Data Insights and Anomaly Detection

## Overview

This project demonstrates a real-time anomaly detection pipeline using Apache Flink (PyFlink) and Apache Kafka. The pipeline ingests streaming sensor data, identifies anomalies in near real-time, and outputs them to standard logs. This setup mimics a production-grade data engineering environment and is highly relevant for enterprises requiring continuous monitoring and fast response systems.

---

## Why This Project Matters

In modern industries, detecting anomalies in streaming data is crucial for operational efficiency, risk mitigation, and customer satisfaction:

Manufacturing: Detect faulty equipment readings, prevent machine breakdowns, and reduce downtime.

Banking/Finance: Monitor transaction streams for fraud detection or unusual trading patterns.

Entertainment & Hospitality: Track real-time user interactions or system metrics to detect service disruptions or unusual behavior.

Real-time processing ensures that businesses can act immediately, rather than relying on batch analytics, which may be too slow for critical decision-making.

---

## Project Setup (WSL-based)

This project was developed on Windows Subsystem for Linux (WSL) to simulate a production-like Linux environment:

### 1. Apache Kafka & Zookeeper:

- Zookeeper and Kafka were installed locally.

- Kafka topics created:

```python
bin/kafka-topics.sh --create --topic sensor-data_2 --bootstrap-server localhost:9092
```

> [!NOTE]
> Interested readers may also check another similar Flink project here: https://github.com/manuelbomi/Flink-and-Kafka-Based-Real-Time-Data-Engineering-Pipeline    for furthe insights on how to set up the project
> 

- Producer streams sensor events into Kafka:

```python
bin/kafka-console-producer.sh --topic sensor-data_2 --bootstrap-server localhost:9092
```

- Consumer can validate incoming events:

  ```python
  bin/kafka-console-consumer.sh --topic sensor-data_2 --bootstrap-server localhost:9092 --from-beginning
  ```

  ---

  ### 2. Apache Flink Cluster:

- Flink standalone cluster setup (start-cluster.sh) with a JobManager and TaskManager, mirroring a minimal production deployment.

- Flink UI accessible at http://localhost:8081 for job monitoring, metrics, and parallelism inspection.

---

## PyFlink Job: Key Components

### 1. Kafka Source Integration:

The Flink job consumes Kafka topic sensor-data_2 using a KafkaSource with SimpleStringSchema.

### 2. Data Transformation:

- Events are parsed using a MapFunction (ParseEvent) to extract sensor_id and value.

- Keyed by sensor_id to isolate sensor streams.

### 3. Sliding Window Anomaly Detection:

- Sliding windows of 10 seconds with a 5-second slide detect anomalies in near real-time.

- Anomalies are flagged if a sensor reading deviates by more than 50 units from the current window average.

### 4. Sliding Window Anomaly Detection:

- Sliding windows of 10 seconds with a 5-second slide detect anomalies in near real-time.

- Anomalies are flagged if a sensor reading deviates by more than 50 units from the current window average.

  ```python
ANOMALY → sensor_1: value=150.0, avg=59.21
ANOMALY → sensor_1: value=180.0, avg=112.5
ANOMALY → sensor_1: value=45.0, avg=112.5
```

