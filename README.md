# fasTools
A Rust reimplementation of [SeqKit](https://github.com/shenwei356/seqkit) 

## Usage

```shell
fasTools <args> <file>
```


### Args list

```shell
--clean # clean up and normalize fasta/fastq records
```


## Test files
The fasta test files are from [Rosalind](https://rosalind.info/problems/list-view/). <br>



### TODO from `seqkit seq`
# fasTools — `seq` subcommand

## Core I/O
- [ ] gzip input support (`flate2`)
- [ ] stdin support (no file argument)
- [ ] output to file (`-o`)

## Sequence transformation
- [x] complement (`-p`)
- [x] reverse complement (`-r -p`)
- [ ] reverse only (`-r`)
- [ ] upper case (`-u`)
- [ ] lower case (`-l`)
- [ ] DNA to RNA (`--dna2rna`)
- [ ] RNA to DNA (`--rna2dna`)
- [ ] remove gaps (`-g`, gap letters via `-G`)

## Filtering
- [ ] min length (`-m`)
- [ ] max length (`-M`)
- [ ] min quality (`-Q`)
- [ ] max quality (`-R`)
- [ ] pattern match by ID (`--f-pattern`)
- [ ] pattern match by sequence (`--f-by-seq`)
- [ ] pattern from file (`--f-pattern-file`)
- [ ] invert match (`--f-invert-match`)
- [ ] ignore case in match (`--f-ignore-case`)
- [ ] full name match (`--f-by-name`)
- [ ] positive strand only (`--f-only-positive-strand`)
- [ ] regex patterns (`--f-use-regexp`)

## Output control
- [ ] headers only (`-n`)
- [ ] IDs only (`-i`)
- [ ] sequences only (`-s`)
- [ ] qualities only (`-q`)
- [ ] colorize output (`-k`)
- [ ] validate bases (`-v`)
- [ ] quality ASCII base (`-b`, default 33)