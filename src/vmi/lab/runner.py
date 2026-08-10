"""
VMI Lab Runner

Central orchestration layer for VMI.

The Lab is intended to become the single entry point for:

- validation
- analysis
- testing
- evaluation
- observability
- training preparation
- future model benchmarking
"""

import json
import subprocess
import sys
import time
from pathlib import Path


class VMILab:

    def __init__(self, project_root=None):
        self.root = Path(
            project_root or Path.cwd()
        ).resolve()

    def environment(self):
        return {
            "python": sys.version,
            "project_root": str(self.root),
            "src_exists": (self.root / "src").exists(),
            "tests_exists": (self.root / "tests").exists(),
            "schemas_exists": (self.root / "schemas").exists(),
            "observatory_exists": (
                self.root / "observatory"
            ).exists(),
        }

    def run_tests(self):
        started = time.time()

        process = subprocess.run(
            [
                sys.executable,
                "-m",
                "pytest",
                "-q",
            ],
            cwd=self.root,
            capture_output=True,
            text=True,
        )

        return {
            "success": process.returncode == 0,
            "return_code": process.returncode,
            "duration_seconds": (
                time.time() - started
            ),
            "stdout": process.stdout,
            "stderr": process.stderr,
        }

    def inspect(self):
        files = []

        important_roots = [
            "src",
            "tests",
            "schemas",
            "docs",
            "training",
            "inference",
            "observatory",
        ]

        for root in important_roots:
            path = self.root / root

            if not path.exists():
                continue

            for item in path.rglob("*"):
                if item.is_file():
                    if "__pycache__" not in item.parts:
                        files.append(
                            str(item.relative_to(self.root))
                        )

        return {
            "file_count": len(files),
            "files": sorted(files),
        }

    def run(self):
        report = {
            "lab": "VMI Lab",
            "version": "0.1",
            "started": time.time(),
            "environment": self.environment(),
        }

        report["project"] = self.inspect()
        report["tests"] = self.run_tests()

        report["completed"] = time.time()

        return report


def main():
    lab = VMILab()

    report = lab.run()

    print(
        json.dumps(
            report,
            indent=2,
            ensure_ascii=False,
        )
    )

    raise SystemExit(
        0 if report["tests"]["success"] else 1
    )


if __name__ == "__main__":
    main()
