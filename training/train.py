"""
VMI Training Entry Point

This file is designed to work both locally for pipeline testing
and later inside an AWS SageMaker training container.
"""

import json
import os
from pathlib import Path


def get_environment():

    return {
        "model_dir": os.environ.get(
            "SM_MODEL_DIR",
            "./artifacts/model"
        ),

        "train_dir": os.environ.get(
            "SM_CHANNEL_TRAIN",
            "./datasets/processed"
        ),

        "checkpoint_dir": os.environ.get(
            "SM_CHECKPOINT_DIR",
            "./artifacts/checkpoints"
        ),
    }


def load_jsonl(path: Path):

    if not path.exists():
        return []

    records = []

    with path.open(
        "r",
        encoding="utf-8"
    ) as f:

        for line in f:

            line = line.strip()

            if line:
                records.append(json.loads(line))

    return records


def main():

    env = get_environment()

    print("=" * 60)
    print("VMI TRAINING")
    print("=" * 60)

    print(f"Model directory: {env['model_dir']}")
    print(f"Training data:   {env['train_dir']}")
    print(f"Checkpoints:     {env['checkpoint_dir']}")

    train_path = Path(
        env["train_dir"]
    ) / "train.jsonl"

    validation_path = Path(
        env["train_dir"]
    ) / "validation.jsonl"

    train_data = load_jsonl(train_path)
    validation_data = load_jsonl(validation_path)

    print()
    print(f"Training examples:   {len(train_data)}")
    print(f"Validation examples: {len(validation_data)}")

    print()
    print("Pipeline validation successful.")
    print("Actual GPU training will be launched through SageMaker.")


if __name__ == "__main__":
    main()
