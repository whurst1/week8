#!/usr/bin/env python
#introduction and rules
UsrName= input("Enter Name Here: ")
print((UsrName),",enter (1) to translate a protein-coding nucleotide sequence to amino acids -or- (2) randomly draw a codon from the sequence.")
#creating paths
Choice= input("Option: ")
if Choice == "1":
	print("You have chosen option 1. Enter Sequence to be translated: ", end ="")
#translate DNA to RNA
	DNASeq= input()
	DNASeq= DNASeq.upper()
	RNASeq= DNASeq.replace("T","U")
#Dictionary
	CodonTrans = {"AAA":"K", "AAC":"N", "AAG":"K", "AAU":"N",
                "ACA":"T", "ACC":"T", "ACG":"T", "ACU":"T",
                "AGA":"R", "AGC":"S", "AGG":"R", "AGU":"S",
                "AUA":"I", "AUC":"I", "AUG":"M", "AUU":"I",
                "CAA":"Q", "CAC":"H", "CAG":"Q", "CAU":"H",
                "CCA":"P", "CCC":"P", "CCG":"P", "CCU":"P",
                "CGA":"R", "CGC":"R", "CGG":"R", "CGU":"R",
                "CUA":"L", "CUC":"L", "CUG":"L", "CUU":"L",
                "GAA":"E", "GAC":"D", "GAG":"E", "GAU":"D",
                "GCA":"A", "GCC":"A", "GCG":"A", "GCU":"A",
                "GGA":"G", "GGC":"G", "GGG":"G", "GGU":"G",
                "GUA":"V", "GUC":"V", "GUG":"V", "GUU":"V",
                "UAA":"_", "UAC":"Y", "UAG":"_", "UAU":"T",
                "UCA":"S", "UCC":"S", "UCG":"S", "UCU":"S",
                "UGA":"_", "UGC":"C", "UGG":"W", "UGU":"C",
                "UUA":"L", "UUC":"F", "UUG":"L", "UUU":"F"}
#translate to AA
	AASeq= ""
	for n in range(0, len(RNASeq), 3):
		if RNASeq[n:n+3] in CodonTrans:
			AASeq += CodonTrans[RNASeq[n:n+3]]
	print("Amino Acid Sequence: ", end = "")
	print(AASeq)
elif Choice == "2":
	print ("You have chosen to randomly draw a codon from the sequence. Enter sequence to be translated: ", end ="")
	DNASeq= input()
	DNASeq= DNASeq.upper()
	RNASeq= DNASeq.replace("T","U")
	RanCodon= [RNASeq[i:i+3] for i in range(0, len(RNASeq), 3)]
#chose random codon
	import random
	RandomCodon= random.choice(RanCodon)
	print(RandomCodon)
#incase they select option that isnt 1 or 2
else:
	print("INVALID OPTION")

