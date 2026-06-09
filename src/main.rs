use std::fs::File;
use std::io::{self, BufRead, BufReader};

struct FastaRecord {
    header: String,
    seq: String
}

struct FastqRecord {
    header: String,
    seq: String,
    q_score: String
}

enum FastxFormat {
    Fasta,
    Fastq
}

enum FastxParse {
    Fasta(FastaRecord),
    Fastq(FastqRecord),
}

fn main() {
    let file = std::env::args().nth(1).expect("Please provide a filepath");
    
    let records: Vec<FastxParse> = match read_fastx_type(&file) {
        Ok(FastxFormat::Fasta) => { 
            read_fasta(&file)
            .into_iter()
            .map(FastxParse::Fasta)
            .collect()
        },
        Ok(FastxFormat::Fastq) => { 
            read_fastq(&file)
            .into_iter()
            .map(FastxParse::Fastq)
            .collect()
        },
        Err(e) => {
            eprintln!("Error: {e}");
            return;
        },
    };

    for record in &records {
        match record {
            FastxParse::Fasta(r) => println!("{}\n{}", r.header, r.seq),
            FastxParse::Fastq(r) => println!("{}\n{}\n{}", r.header, r.seq, r.q_score),
        }
    }

}


fn read_fastx_type(file: &str) -> Result<FastxFormat, io::Error> {  
    let fastx_file = File::open(file)?;
    let mut reader = BufReader::new(fastx_file);
    let mut first_line = String::new();

    reader.read_line(&mut first_line)?;

    match first_line.chars().next() {
        Some('>') => Ok(FastxFormat::Fasta),
        Some('@') => Ok(FastxFormat::Fastq),
        _ => Err(io::Error::new(io::ErrorKind::InvalidData, "Not a valid fasta/fastq file")),
    }
}

fn read_fasta(file: &str) -> Vec<FastaRecord> {
    let mut records = Vec::new();
    let mut current_header: Option<String> = None;
    let mut current_seq = String::new();

    let reader = BufReader::new(File::open(file).expect("valid file"));

    for line in reader.lines() {
        let line = line.unwrap();
        let line = line.trim();
        
        if line.is_empty() {
            continue;
        }

        if line.starts_with('>') {
            if let Some(header) = current_header.take() {
                records.push(FastaRecord {
                    header,
                    seq: current_seq.clone()
                });
                current_seq.clear();
            }

            current_header = Some(line[1..].to_string());
        } else {
            current_seq.push_str(line);
        }
    }

    if let Some(header) = current_header.take() {
        records.push(FastaRecord {
            header,
            seq: current_seq
        });
    }

    records
}


fn read_fastq(file: &str) -> Vec<FastqRecord> { 
    let mut records = Vec::new();
    let mut current_header = String::new();
    let mut current_seq = String::new();

    let reader = BufReader::new(File::open(file).expect("Invalid file, try again"));

    let mut line_number: usize = 0;

    for line in reader.lines() {
        let line = line.unwrap();
        let line = line.trim();
        if line.is_empty() {
            continue;
        }

        match line_number % 4 {
            0 => { current_header = line.to_string() },
            1 => { current_seq = line.to_string() },
            2 => { },
            3 => { records.push(FastqRecord {
                header: current_header.clone(), 
                seq: current_seq.clone(),
                q_score: line.to_string(),
                });
            },
            _ => { },
        };

        line_number += 1;
    }
    records
}



fn parse_gzip() { todo!() } // use flate2 