# SPDX-License-Identifier: GPL-3.0-only
# PlatformIO post-build step (as gencord's): the app image for an M5Launcher slot, and the full image for a bare
# Cardputer, next to the project: amb-cardputer.bin, amb-cardputer.full.bin.
import shutil
from pathlib import Path

Import("env")  # noqa: F821


def copy_bin(source, target, env):
    build = Path(env.subst("$BUILD_DIR"))
    out = Path(env.subst("$PROJECT_DIR"))
    shutil.copyfile(build / "firmware.bin", out / "amb-cardputer.bin")
    if (build / "firmware.factory.bin").exists():
        shutil.copyfile(build / "firmware.factory.bin", out / "amb-cardputer.full.bin")
    print("amb-cardputer.bin updated")


env.AddPostAction("$BUILD_DIR/${PROGNAME}.bin", copy_bin)  # noqa: F821
