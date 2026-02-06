# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Context

GATS2128N inspection equipment cycle time investigation (Issue: AJ005422).
This directory contains system logs, debug logs, configuration snapshots, and utility scripts for analyzing W618 cycle time performance issues.

## Directory Layout

- `LOG/` - Main system log (20260203.LOG, ~1.8GB) and utilities
- `DEBUG LOG/ChkSerial/`, `ChkStockerLog/`, `ChkTQACount/` - Hourly debug logs from subsystems
- `RECIPE/` - Product test recipe (JYK172-READ-02) with alignment, config, version files
- `SYSTEM/` - Equipment configuration (GSP, PAR, INI files for GATS2120 variant)

## Log Format

Main log is comma-separated with ISO timestamps:
```
[counter],[Component::Function],[ACT/ACK],[status],[params],...,[YYYY/MM/DD HH:MM:SS]
```

## Utilities

- `split_file.py` - Splits files >100MB into 100MB chunks. Run: `python split_file.py [filepath]`

## Key Configuration

- System type: GATS2120 (Custom.gsp SystemType=7)
- Stocker slots: PASS(1), OPEN(3), LEAK(5), 4W(6), ALIGN(7), LCR(11), Notch(12), 2DCode Error(5)
- Test categories: 19 failure modes defined in YieldBin.ini
