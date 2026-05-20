import os

LABEL_DIRS = [
    "temp_rust_1/train/labels",
    "temp_rust_1/valid/labels",
    "temp_rust_2/train/labels",
    "temp_rust_2/valid/labels",
]

for label_dir in LABEL_DIRS:

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

                # Convert rust class to ID 1
                parts[0] = "1"

                updated_lines.append(" ".join(parts))

        with open(file_path, "w") as file:
            file.write("\n".join(updated_lines))

print("Rust labels converted to class ID 1 successfully.")