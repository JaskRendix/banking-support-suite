import re
from collections import Counter


def analyze_logs(file_path: str) -> None:
    """Parses application logs to count error types."""
    error_patterns = {"FATAL": r"\[FATAL\]", "ERROR": r"\[ERROR\]", "WARN": r"\[WARN\]"}

    stats: Counter[str] = Counter()

    try:
        with open(file_path, "r") as file:
            for line in file:
                for level, pattern in error_patterns.items():
                    if re.search(pattern, line):
                        stats[level] += 1

        print("--- Daily Log Summary ---")
        for level, count in stats.items():
            print(f"{level}: {count} occurrences")

    except FileNotFoundError:
        print(f"Error: Log file {file_path} not found.")


if __name__ == "__main__":
    import sys
    from pathlib import Path

    if len(sys.argv) < 2:
        print("Usage: python log_analyzer.py <log_file_path>")
    else:
        log_path = Path(sys.argv[1])
        analyze_logs(log_path.as_posix())
