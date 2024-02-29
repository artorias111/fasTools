#!/usr/bin/env python3

### codon table : - table from https://gist.github.com/juanfal
codontab = {
    'TCA': 'S',    # Serina
    'TCC': 'S',    # Serina
    'TCG': 'S',    # Serina
    'TCT': 'S',    # Serina
    'TTC': 'F',    # Fenilalanina
    'TTT': 'F',    # Fenilalanina
    'TTA': 'L',    # Leucina
    'TTG': 'L',    # Leucina
    'TAC': 'Y',    # Tirosina
    'TAT': 'Y',    # Tirosina
    'TAA': '*',    # Stop
    'TAG': '*',    # Stop
    'TGC': 'C',    # Cisteina
    'TGT': 'C',    # Cisteina
    'TGA': '*',    # Stop
    'TGG': 'W',    # Triptofano
    'CTA': 'L',    # Leucina
    'CTC': 'L',    # Leucina
    'CTG': 'L',    # Leucina
    'CTT': 'L',    # Leucina
    'CCA': 'P',    # Prolina
    'CCC': 'P',    # Prolina
    'CCG': 'P',    # Prolina
    'CCT': 'P',    # Prolina
    'CAC': 'H',    # Histidina
    'CAT': 'H',    # Histidina
    'CAA': 'Q',    # Glutamina
    'CAG': 'Q',    # Glutamina
    'CGA': 'R',    # Arginina
    'CGC': 'R',    # Arginina
    'CGG': 'R',    # Arginina
    'CGT': 'R',    # Arginina
    'ATA': 'I',    # Isoleucina
    'ATC': 'I',    # Isoleucina
    'ATT': 'I',    # Isoleucina
    'ATG': 'M',    # Methionina
    'ACA': 'T',    # Treonina
    'ACC': 'T',    # Treonina
    'ACG': 'T',    # Treonina
    'ACT': 'T',    # Treonina
    'AAC': 'N',    # Asparagina
    'AAT': 'N',    # Asparagina
    'AAA': 'K',    # Lisina
    'AAG': 'K',    # Lisina
    'AGC': 'S',    # Serina
    'AGT': 'S',    # Serina
    'AGA': 'R',    # Arginina
    'AGG': 'R',    # Arginina
    'GTA': 'V',    # Valina
    'GTC': 'V',    # Valina
    'GTG': 'V',    # Valina
    'GTT': 'V',    # Valina
    'GCA': 'A',    # Alanina
    'GCC': 'A',    # Alanina
    'GCG': 'A',    # Alanina
    'GCT': 'A',    # Alanina
    'GAC': 'D',    # Acido Aspartico
    'GAT': 'D',    # Acido Aspartico
    'GAA': 'E',    # Acido Glutamico
    'GAG': 'E',    # Acido Glutamico
    'GGA': 'G',    # Glicina
    'GGC': 'G',    # Glicina
    'GGG': 'G',    # Glicina
    'GGT': 'G'     # Glicina
}

class fasta:
    def __init__(self, filepath):
        self.filepath = filepath

    def read_fasta_file(self):
        with open (self.filepath,'r') as f :
            d={} # output dictionary
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

    def fasta_length(self):
        d=self.read_fasta_file() # Read the fasta file
        l={} # dictionary that stores "scaffold_name:size"
        for i in d:
            l[i]=len(d[i])        
        return l

    def get_gc_count(s): # s is a string
        for i in s:
            gc_count=0
            if i=='G' or i=='C' or i=='g' or i=='c':
                gc_count+=1
        return gc_count

    def gc_content(self):
        d=self.read_fasta_file()
        l=self.fasta_length()
        gc={} # A dictionary that stores "scaffold_name:gc_fraction"
        for i in d:
            gc[i]=fasta.get_gc_count(d[i])/len(d[i])

        return gc

    # def k-mer_composition(self): 

   # def translate(self): for all 3 (6?) reading frames 

if __name__=="__main__":
    print("Script for handling fasta file functions")

    # Dev Tests
    f=fasta('../tests/fasta_test_files/grph.fa')
    # print(f.read_fasta_file)
    # print(f.fasta_length())
    print(f.gc_content())