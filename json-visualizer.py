import json
import argparse
import matplotlib.pyplot as plt
from collections import Counter
from pathlib import Path

def main():
    # Positional argument for the JSON file path
    parser = argparse.ArgumentParser(
        description="Visualize number of processes per user from a JSON file."
    )
    parser.add_argument("filepath", help="Path to the JSON file (e.g., processes.json)")
    args = parser.parse_args()

    # Resolve the file path
    json_path = Path(args.filepath).expanduser().resolve()
    if not json_path.exists():
        print(f"Error: File not found at {json_path}")
        return

    # Load JSON
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Extract and normalize User field
    users = [proc.get("User", "N/A") or "N/A" for proc in data]  # handles None and missing values
    process_count = Counter(users)
    sorted_users = sorted(process_count.items(), key=lambda x: x[1], reverse=True)

    # Prepare data for plotting
    user_names, user_counts = zip(*sorted_users)

    # Plot
    plt.figure(figsize=(12, 6))
    plt.bar(user_names, user_counts)
    plt.title("Number of Processes per User")
    plt.xlabel("User")
    plt.ylabel("Number of Processes")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
