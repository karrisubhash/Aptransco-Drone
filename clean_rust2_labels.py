import os

LABEL_DIRS = [
    "temp_rust_2/train/labels",
    "temp_rust_2/valid/labels",
    "temp_rust_2/test/labels",
]

for label_dir in LABEL_DIRS:

    if not os.path.exists(label_dir):
        continue

    for filename in os.listdir(label_dir):

        if not filename.endswith(".txt"):
            continue

        file_path = os.path.join(label_dir, filename)

        cleaned_lines = []

        with open(file_path, "r") as file:

            lines = file.readlines()

            for line in lines:

                parts = line.strip().split()

                if not parts:
                    continue

                class_id = parts[0]

                # REMOVE invalid class 0
                if class_id == "0":
                    continue

                # Convert Corrosions → rust
                if class_id == "1":
                    parts[0] = "0"

                cleaned_lines.append(" ".join(parts))

        with open(file_path, "w") as file:
            file.write("\n".join(cleaned_lines))

print("Rust Dataset 2 labels cleaned successfully.")