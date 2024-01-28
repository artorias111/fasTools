#!/usr/bin/env python3 


def read_fasta_file(filename):
# Takes a fasta file and returns a dictionary with key:value as header:sequence
# Warning : The sequence is returned as a single string, be wary of memory usage
# Works with both single line and multiline fasta
    d = {} # output dictionary
    with open (filename,'r') as f :
        for line in f :
            l=line.strip()
            if l=="":
                continue
            if l[0]==">":
                d[l[1:]]=""
                tmp=l[1:]
                continue
            d[tmp]+=l
    return d



def fasta_len(filename):
# Takes a fasta file, and returns the size of each contig in terms of base pairs

    l={} # output dictionary
    d=read_fasta_file(filename)
    for i in d:
        


def gc_content(filename):
# Returns a GC content summary of a fasta file. Per contig and overall

    # Read the fasta file and store it in a dictionary
    d=read_fasta_file(filename)
    for i in d:


# def k-mer_composition
# 




if __name__=="__main__":
    print("Script for handling fasta file functions")

    # DevTests
    f=read_fasta_file("../tests/fasta_test_files/grph.fa")