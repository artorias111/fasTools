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
- [x] reverse only (`-r`)
- [x] upper case (`-u`)
- [x] lower case (`-l`)
- [x] DNA to RNA (`--dna2rna`)
- [x] RNA to DNA (`--rna2dna`)
- [x] remove gaps (`-g`, gap letters via `-G`)

## Filtering
- [x] min length (`-m`)
- [x] max length (`-M`)
- [ ] min quality (`-Q`)
- [ ] max quality (`-R`)
- [x] pattern match by ID (`--f-pattern`)
- [x] pattern match by sequence (`--f-by-seq`)
- [ ] pattern from file (`--f-pattern-file`)
- [ ] invert match (`--f-invert-match`)
- [ ] don't ignore case in match (`--f-no-ignore-case`)
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
