#!/usr/bin/env python3

class fastq:
    def __init__(self, filepath):
        self.filepath = filepath


    def read_fastq_file(self):
        with open (self.filepath,'r') as f :
            # Sequence dictionary stored as header:sequence
            fq_seq={}
            # Sequence dictionary stored as header:phred scores
            fq_phred={}
            for line in f:
                l=line.strip()
                if l=="":
                    continue
                if l[0]=="@":
                    fq_seq[l[1:]]=""
                    fq_phred[l[1:]]=""
                    tmp=l[1:]
                    ctr=1
                    continue
                if l[0]=="+":
                    ctr=0
                    continue
                if ctr==1:
                    fq_seq[tmp]+=l
                    ctr=0
                    continue
                else:
                    fq_phred[tmp]+=l
                    ctr=0
        return fq_seq,fq_phred

    def get_seqs(self): # If you want to convert the fastq to fasta for some reason
        fq_seq,_=fastq.read_fastq_file(self)
        return(fq_seq)

    def get_phred_scores(self):
        _,fq_phred=fastq.read_fastq_file(self)
        return fq_phred


if __name__=="__main__":
    print("Script for handling fastq file functions")

    # Dev Tests : Load more test files to figure out edge cases
    f=fastq('../tests/fastq_test_files/1_control_psbA3_2019_minq7.fastq')
    # print(f.read_fastq_file())
    print(f.get_seqs())
