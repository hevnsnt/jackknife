# Jackknife - Simulated PoC (Tabletop Exercise Artifact)

**This repository contains no real exploit code.** Everything here is a
labeled, non-functional simulation built for a Trifident Advisory Services
tabletop exercise (TTX) run with Zebra Technologies in November 2026.

## What this is

A single Python script, `jackknife_poc.py`, styled to look like a
proof-of-concept exploit, for use as a discussion artifact during the
exercise. It is meant to look the part on screen during a facilitated
walkthrough, nothing more.

- The vulnerability name "Jackknife" and the ID `CVE-2026-XXXXX` are
  **fictional**. They do not correspond to any real CVE.
- The "library" referenced in the script's output is a placeholder name,
  not a real package.
- There is no obfuscation anywhere in this repository. Every line is
  plain, commented Python you can read top to bottom in under a minute.

## What this is not

- Not a working exploit. It does not implement, demonstrate, or enable
  any real attack technique.
- Not network-capable. It opens no sockets, makes no requests, and
  contacts no host.
- Not a general-purpose security tool. Do not adapt it into one.

## What the script actually does

Running it prints a short, clearly-labeled narrative ("Step 1 - Simulated
recon", etc.) describing what a real exploit chain would hypothetically
do at each stage, for exercise participants to read and discuss. No file
I/O beyond printing to stdout, no subprocess calls, no network calls, no
dynamic code execution, no encoded or hidden payloads.

Each step also prints a short cosmetic line of simulated "tool chatter"
in Chinese, styled to look like captured output from a real intrusion
tool for realism during the exercise. Every one of those lines is
immediately followed by its English translation in the same output, so
nothing in this repo is ever presented untranslated or left to be taken
on faith. Use of Chinese-language flavor text here is exercise styling
only and is not intended to represent, attribute, or imply involvement
of any real individual, organization, or nation-state.

```
python3 jackknife_poc.py --i-understand-this-is-fake
```

The `--i-understand-this-is-fake` flag is required on purpose, as a
reminder before anyone runs it that this is exercise material.

## Why it's public

This repo exists to support a live tabletop exercise where participants
may be asked to look at "found" artifacts, including something that
resembles a PoC. It is public, readable, and inert so that nothing about
it needs to be taken on faith: open the script and read it.

## License / use

Provided as-is for tabletop exercise purposes. Do not represent this as,
or repurpose this into, a real security tool.
