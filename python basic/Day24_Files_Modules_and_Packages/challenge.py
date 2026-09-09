"""
============================================================
DAY 24 CHALLENGE & MINI-PROJECT
============================================================

PROJECT: Web Server Access Log Analyzer & Rotation Engine

In real backend architectures (Nginx, Gunicorn, Django), access logs
provide critical observability into system health, error spikes, and
slow endpoints.

Log Line Format:
  <IP> - [<TIMESTAMP>] "<METHOD> <PATH> HTTP/1.1" <STATUS_CODE> <RESPONSE_TIME_MS>

Example Log Line:
  192.168.1.15 - [2026-09-06T10:00:00] "GET /api/v1/products HTTP/1.1" 200 45

============================================================
REQUIREMENTS:
============================================================
1. Build class `AccessLogAnalyzer`:
   - `__init__(self, log_file: Path)`: Store log file path.
   - `parse_logs() -> list[dict]`:
     - Reads the log file line by line defensively.
     - Ignores blank lines or lines that cannot be parsed.
     - Extracts: `ip`, `timestamp`, `method`, `path`, `status_code` (int), and `response_time_ms` (int).
   - `generate_metrics() -> dict`:
     - Computes:
       * `total_requests`: int
       * `status_codes`: dict breakdown e.g. {"2xx": count, "4xx": count, "5xx": count, "other": count}
       * `error_rate`: float percentage of 4xx and 5xx errors (e.g. 25.0%)
       * `avg_response_time_ms`: float average response time
       * `slowest_endpoint`: str path with the highest single response time
   - `export_summary_json(output_file: Path) -> None`:
     - Writes metrics to a JSON report formatted with 4-space indent.
   - `rotate_if_exceeds(max_bytes: int, archive_dir: Path) -> bool`:
     - If the log file size exceeds `max_bytes`:
       - Moves it to `archive_dir / f"access_archive_{timestamp}.log"`.
       - Creates a fresh, empty file at the original `log_file` path.
       - Returns True.
     - Otherwise returns False.
"""

import json
import re
from pathlib import Path
from datetime import datetime


class AccessLogAnalyzer:
    def __init__(self, log_file: Path):
        self.log_file = Path(log_file)

    def parse_logs(self) -> list[dict]:
        """
        Parses log entries into structured dictionaries.
        Handle FileNotFoundError by returning an empty list.
        
        """
        log=[]
        try:
          with open(self.log_file,"r",encoding="utf-8")as file:
            for reader in file:
              parts=reader.split()
              if not parts:
                continue
            #`ip`, `timestamp`, `method`, `path`, `status_code` (int), and `response_time_ms` (int).
            #192.168.1.15 - [2026-09-06T10:00:00] "GET /api/v1/products HTTP/1.1" 200 45
              entry={
                "ip":parts[0],
                "timestamp":parts[2].strip("[]"),
                "method":parts[3].strip('""'),
                "path":parts[4],
                "status_code":int(parts[6]),
                "response_time_ms":int(parts[7])
                 }
              log.append(entry)        
        except FileNotFoundError:
            return []
        return log  


    def generate_metrics(self) -> dict:
        """
        Calculates aggregate statistics: total requests, status code distribution,
        error rates, and average response times.
        
        """
        store=self.parse_logs()
        total_request=len(store)
        if total_request == 0:
          return{
            "total_request":0,
            "status_counts":{"2xx":0,"3xx":0,"4xx":0,"5xx":0,"other":0},
            "error_rate":0,
            "average_respnosetime":0,
            "slowest_endpint":None
            
          }
        
        print(f"total request {len(store)}")
        sum_responsetime=0
        error=0
        
        status_counts={"2xx":0,"3xx":0,"4xx":0,"5xx":0,"other":0}
        slowest_endpoint=""
        max_resposne_time=-1
        for record in store:
          print(record["status_code"])
          resp_time=record["response_time_ms"]
          
          if 200 <= record["status_code"]<300:
            status_counts["2xx"] +=1
          elif 300<=record["status_code"] <400:
            status_counts["3xx"] +=1
          elif 400 <=record["status_code"] <500:
            status_counts["4xx"] +=1
          elif 500 <=record["status_code"] <600:
            status_counts["5xx"] +=1
          else:
            status_counts["other"] +=1
            
          
          if record["status_code"] >=400:
            error +=1
            
          sum_responsetime= sum_responsetime + record["response_time_ms"]  

          if  resp_time>max_resposne_time:
            max_resposne_time=resp_time
            slowest_endpoint =record["path"]
        print("slow : ",slowest_endpoint)
      
      
        average_respnosetime=sum_responsetime/len(store)
        # print("Average :",average)
        error_rate=error/len(store)*100
        # print("Error rate :",error_rate)
        return{
          "total_request":total_request,
              "status_counts":{"2xx":status_counts["2xx"],"3xx":status_counts["3xx"],"4xx":status_counts["4xx"],"5xx":status_counts["5xx"],"other":status_counts["other"]},
              "error_rate":error_rate,
              "average_respnosetime":average_respnosetime,
              "slowest_endpint":slowest_endpoint  
        }
       
      

    def export_summary_json(self, output_file: Path) -> None:
        """
        Exports the metrics dictionary to a JSON file.
        """
        # TODO: Save metrics using json.dump with indent=4
        pass

    def rotate_if_exceeds(self, max_bytes: int, archive_dir: Path) -> bool:
        """
        Rotates the current log file to archive_dir if size > max_bytes.
        """
        # TODO: Check file size, rename/move if needed, create fresh empty file
        pass


# ============================================================
# VERIFICATION SUITE
# ============================================================
if __name__ == "__main__":
    work_dir = Path(__file__).resolve().parent / "test_logs"
    work_dir.mkdir(exist_ok=True)
    
    sample_log = work_dir / "access.log"
    sample_data = """192.168.1.1 - [2026-09-06T10:00:01] "GET /api/v1/products HTTP/1.1" 200 45
192.168.1.2 - [2026-09-06T10:00:02] "POST /api/v1/orders HTTP/1.1" 201 120
192.168.1.3 - [2026-09-06T10:00:03] "GET /api/v1/users/999 HTTP/1.1" 404 15
192.168.1.4 - [2026-09-06T10:00:04] "POST /api/v1/checkout HTTP/1.1" 500 850
192.168.1.5 - [2026-09-06T10:00:05] "GET /api/v1/products HTTP/1.1" 200 50
"""
    sample_log.write_text(sample_data, encoding="utf-8")
    
    analyzer = AccessLogAnalyzer(sample_log)
    print("Testing AccessLogAnalyzer...")
    records = analyzer.parse_logs()
    print(f"Parsed records count: {len(records) if records else 0}")
    
    metrics = analyzer.generate_metrics()
    print(f"Metrics output: {metrics}")
    
    report_file = work_dir / "report.json"
    analyzer.export_summary_json(report_file)
    if report_file.exists():
        print(f"Report successfully saved to {report_file.name}")
        print(report_file.read_text(encoding="utf-8"))
        
    # Test rotation
    archive_folder = work_dir / "archive"
    rotated = analyzer.rotate_if_exceeds(max_bytes=100, archive_dir=archive_folder)
    print(f"File rotated (threshold 100 bytes): {rotated}")
    
    # Clean up test artifacts
    import shutil
    shutil.rmtree(work_dir)
    print("Test cleanup complete.")