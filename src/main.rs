use std::fs::File;
use std::io::{self, BufRead, BufReader};

struct fasta_record {
    name: String,
    seq: String
};

struct fastq_record {
    name: String,
    seq: String,
    q_score: String
};

enum fastx_kind {
    fasta,
    fastq,
}


fn main() {
    let file = std::env::args();
    let mut reader = read_fastx_type(file);
}


fn read_fastx_type(file: &str) ->  {  // placeholder iterator of some kind
    let fastx_file = File::open(file)?;
    
}