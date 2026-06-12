import json
from datetime import datetime

def check_vital_signs(pulse_rate):
    """Business logic utility to flag abnormal pulse rates instantly."""
    if pulse_rate < 60:
        return "BRADYCARDIA_ALERT"
    elif pulse_rate > 100:
        return "TACHYCARDIA_ALERT"
    return "NORMAL"

def process_pulse_payload(raw_json_string):
    print("Parsing raw patient telemetry payload...")
    try:
        # 1. Parse incoming text into searchable JSON
        data = json.loads(raw_json_string)
        
        # 2. Extract core vitals metrics
        patient_id = data.get("patient_id")
        pulse = int(data.get("pulse_rate", 0))
        
        # 3. Apply operational data quality rules
        status_flag = check_vital_signs(pulse)
        
        # 4. Construct clean analytical output
        processed_record = {
            "patient_id": patient_id,
            "recorded_pulse": pulse,
            "clinical_severity_tag": status_flag,
            "transformation_metadata": {
                "pipeline_version": "v1.2.0",
                "processed_at_utc": datetime.utcnow().isoformat()
            }
        }
        
        print(f"✅ Patient {patient_id} processed safely with status: {status_flag}")
        return processed_record

    except (ValueError, KeyError) as e:
        print(f"❌ Data Quality Dropout: Failed to parse pulse payload. Error: {str(e)}")
        return None

# Simulation block to demonstrate functionality to profile visitors
if __name__ == "__main__":
    mock_payload = '{"patient_id": "PT-7741", "pulse_rate": "112", "device_type": "wearable_v4"}'
    output = process_pulse_payload(mock_payload)
