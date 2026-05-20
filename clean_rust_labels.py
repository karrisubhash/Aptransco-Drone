import os

LABEL_DIRS = [
    "temp_rust_1/train/labels",
    "temp_rust_1/valid/labels",
    "temp_rust_1/test/labels",
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

                # REMOVE tower_main_body
                if class_id == "2":
                    continue

                # Convert severe_corrosion → rust
                if class_id == "1":
                    parts[0] = "0"

                cleaned_lines.append(" ".join(parts))

        with open(file_path, "w") as file:
            file.write("\n".join(cleaned_lines))

print("Rust Dataset 1 labels cleaned successfully.")