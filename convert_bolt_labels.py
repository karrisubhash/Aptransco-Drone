import os

DATASETS = [
    ("temp_missing_bolt/train/labels", "2"),

    ("temp_loose_bolt/train/labels", "3"),
    ("temp_loose_bolt/valid/labels", "3"),
    ("temp_loose_bolt/test/labels", "3"),
]

for label_dir, new_class_id in DATASETS:

    if not os.path.exists(label_dir):
        continue

    for filename in os.listdir(label_dir):

        if not filename.endswith(".txt"):
            continue

        file_path = os.path.join(label_dir, filename)

        updated_lines = []

        with open(file_path, "r") as file:

            lines = file.readlines()

            for line in lines:

                parts = line.strip().split()

                if not parts:
                    continue

                # Convert class ID
                parts[0] = new_class_id

                updated_lines.append(" ".join(parts))

        with open(file_path, "w") as file:
            file.write("\n".join(updated_lines))

print("All bolt dataset labels converted successfully.")