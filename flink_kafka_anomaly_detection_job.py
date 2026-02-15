from pyflink.datastream import StreamExecutionEnvironment
from pyflink.common.watermark_strategy import WatermarkStrategy
from pyflink.datastream.connectors.kafka import KafkaSource
from pyflink.common.serialization import SimpleStringSchema
from pyflink.datastream.window import SlidingProcessingTimeWindows
from pyflink.common.time import Time
from pyflink.datastream.functions import WindowFunction, MapFunction
from pyflink.common import Types


class ParseEvent(MapFunction):
    def map(self, event_str):
        sensor_id, value = event_str.split(",")
        return sensor_id, float(value)


class AnomalyDetectionWindowFunction(WindowFunction):
    def apply(self, key, window, inputs):
        values = [v for (_, v) in inputs]

        if not values:
            return []

        avg = sum(values) / len(values)

        results = []
        for v in values:
            if abs(v - avg) > 50:
                results.append(f"ANOMALY → {key}: value={v}, avg={avg}")

        return results


def main():
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)

    kafka_source = (
        KafkaSource.builder()
        .set_bootstrap_servers("localhost:9092")
        .set_topics("sensor-data_2")   # ✅ FIXED
        .set_group_id("flink-anomaly-group")
        .set_value_only_deserializer(SimpleStringSchema())
        .build()
    )

    ds = env.from_source(
        kafka_source,
        WatermarkStrategy.no_watermarks(),
        "Kafka Source"
    )

    parsed = ds.map(
        ParseEvent(),
        output_type=Types.TUPLE([Types.STRING(), Types.FLOAT()])
    )

    anomalies = (
        parsed
        .key_by(lambda x: x[0])
        .window(SlidingProcessingTimeWindows.of(Time.seconds(10), Time.seconds(5)))
        .apply(AnomalyDetectionWindowFunction(), output_type=Types.STRING())
    )

    anomalies.print()

    env.execute("PyFlink Anomaly Detection v2")


if __name__ == "__main__":
    main()