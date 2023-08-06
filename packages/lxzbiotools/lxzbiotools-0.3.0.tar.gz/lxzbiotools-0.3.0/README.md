## Introduction

**lxzbiotools** contains some bioinformation data processing scripts.

Obviously, it is not perfect, so it will be updated later until it is strong enough

## Install

```
pip3 install lxzbiotools
```

## Use

```bash
$ lxzbiotools --help

 Usage: lxzbiotools [OPTIONS] COMMAND [ARGS]...

 Xingze Li's bioinformatics analysis scripts.
 emali: lixingzee@gmail.com

╭─ Options ──────────────────────────────────────────────────────────────────────────────╮
│ --install-completion        [bash|zsh|fish|powershell|p  Install completion for the    │
│                             wsh]                         specified shell.              │
│                                                          [default: None]               │
│ --show-completion           [bash|zsh|fish|powershell|p  Show completion for the       │
│                             wsh]                         specified shell, to copy it   │
│                                                          or customize the              │
│                                                          installation.                 │
│                                                          [default: None]               │
│ --help                                                   Show this message and exit.   │
╰────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ─────────────────────────────────────────────────────────────────────────────╮
│ cds2pep          Convert cds file to pep file                                          │
│ excel2txt        Convert excel file to txt file                                        │
│ fa2fq            Convert a fasta file to a fastq file                                  │
│ fq2fa            Convert a fastq file to a fasta file                                  │
│ gfa2fa           Convert gfa file to fasta file                                        │
│ gff                                                                                    │
│ len                                                                                    │
│ run              Parallelized running tasks                                            │
│ seq              Extract sequences by sequence name or keyword                         │
│ trans            Convert multi-line fasta to one-line fasta                            │
╰────────────────────────────────────────────────────────────────────────────────────────╯
```