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
> Interested readers may also check another similar Flink project here:    for furthe insights on how to set up the project
> 
