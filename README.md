# AWS Data Engineering & Cloud Architecture Portfolio

Welcome to my cloud engineering portfolio! This repository highlights four distinct production patterns I designed and deployed on AWS, focusing on clinical data optimization, real-time ingestion, system decoupling, and cloud financial governance.

---

## 🏥 Project 1: Clinical Lakehouse Migration Pipeline (Batch Engine)
* **Architecture:** `Amazon S3 Raw Lake` ➔ `AWS Glue PySpark` ➔ `Apache Iceberg / AWS Glue Catalog`
* **Core Concept:** Migrating legacy medical records and patient risk profiles into an optimized, transactional lakehouse schema.
* **Key Achievements:**
  * Designed an ETL pipeline to migrate high-volume patient eligibility and pulse data logs into a high-performance Apache Iceberg layout.
  * Formulated schema optimization strategies to reduce patient eligibility record processing time from over an hour down to three minutes.
  * Configured AWS Glue Catalog metadata synchronization to enable zero-copy querying for downstream analytics warehouses.

---

## 🚀 Project 2: Real-Time Event Streaming Engine
* **Architecture:** `Amazon Kinesis Data Streams` ➔ `AWS Lambda (Python)` ➔ `Amazon CloudWatch`
* **Core Concept:** Real-time event-driven ingestion capable of handling concurrent traffic spikes.
* **Key Achievements:**
  * Deployed a provisioned, multi-shard Kinesis highway to absorb continuous clickstream payloads.
  * Configured native IAM Execution Roles to bridge service communication using zero-trust principles.
  * Developed a serverless Python worker that decodes high-velocity Base64 data bursts into clean analytical JSON objects in real-time.

---

## 🏪 Project 3: High-Throughput Decoupled Microservice
* **Architecture:** `Amazon SQS` ➔ `AWS Lambda`
* **Core Concept:** Asynchronous message queuing to scale applications and protect backend stores.
* **Key Achievements:**
  * Created an enterprise-grade message queue (`live-clickstream-queue`) to act as a buffer for high-traffic apps.
  * Modeled architectural patterns for message retention and workload isolation to prevent downstream system crashes during transaction spikes.

---

## 🔔 Project 4: Serverless Cloud Financial Watchdog
* **Architecture:** `AWS Budgets` ➔ `Amazon SNS`
* **Core Concept:** FinOps governance and automated infrastructure cost monitoring.
* **Key Achievements:**
  * Architected a rigid cost monitoring matrix tracking exact credit burn allocations.
  * Programmed proactive budget threshold triggers designed to fire instantaneous alerts to engineering teams the absolute millisecond consumption flags are raised.
