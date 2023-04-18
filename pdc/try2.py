import multiprocessing
import smithWatermanmod

def smith_waterman_parallel(seq1, seq2):
    return smithWatermanmod.smith_waterman(seq1, seq2)

def main():
    str1="cttcctcgtgagaactgtattgacacccttgtgttgtcacgtttgattcattccaacctcaaggacaccgatatgggtcttctgcgttccggcaagttgcccggaaaacgctttgggtctcacgctttggaggcgtggggttatcgcttaggcgagatgaagggtgaatacaaagacgactttaagcgtatgcttgaagagcagggtgaagaatacgttgacggaatggagtggtggaacttcaacgaagagatgatggactataacgttcaggacgttgtggtaactaaagctctccttgagaagctactctctgacaaacattacttccctcctgagattgactttacggacgtaggatacactacgttctggtcagaatcccttgaggccgttgacattgaacatcgtgctgcatggctgctcgctaaacaagagcgcaacgggttcccgtttgacacaaaagcaatcgaagagttgtacgtagagttagctgctcgccgctctgagttgctccgtaaattgaccgaaacgttcggctcgtggtatcagcctaaaggtggcactgagatgttctgccatccgcgaacaggtaagccactacctaaataccctcgcattaagacacctaaagttggtggtatctttaagaagcctaagaacaaggcacagcgagaaggccgtgagccttgcgaacttgatacccgcgagtacgttgctggtgctccttacaccccagttgaacatgttgtgtttaacccttcgtctcgtgaccacattcagaagaaactccaagaggctgggtgggtcccgaccaagtacaccgataagggtgctcctgtggtggacgatgaggtactcgaaggagtacgtgtagatgaccctgagaagcaagccgctatcgacctcattaaagagtacttgatgattcagaagcgaatcggacagtctgctgagggagacaaagcatggcttcgttatgttgctgaggatggtaagattcatggttctgttaaccctaatggagcagttacgggtcgtgcgacccatgcgttcccaaaccttgcgcaaattccgggtgtacgttctccttatggagagcagtgtcgcgctgcttttggcgctgagcaccatttggatgggataactggtaagccttgggttcaggctggcatcgacgcatccggtcttgagctacgc"
    seq1 = str1.upper()
    str2="gtattgacacccttgtgttgtcacgtttgattcattccaacctcaaggacaccgatatgggtcttctgcgttccggcaagttgcccggaaaacgctttgggtctcacgctttggaggcgtggggttatcgcttaggcgagatgaagggtgaatacaaagacgactttaagcgtatgcttgaagagcagggtgaagaatacgttgacggaatggagtggtggaacttcaacgaagagatgatggactataacgttcaggacgttgtggtaactaaagctctccttgagaagctactctctgacaaacattacttccctcctgagattgactttacggacgtaggatacactacgttctggtcagaatcccttgaggccgttgacattgaacatcgtgctgcatggctgctcgctaaacaagagcgcaacgggttcccgtttgacacaaaagcaatcgaagagttgtacgtagagttagctgctcgccgctctgagttgctccgtaaattgaccgaaacgttcggctcgtggtatcagcctaaaggtggcactgagatgttctgccatccgcgaacaggtaagccactacctaaataccctcgcattaagacacctaaagttggtggtatctttaagaagcctaagaacaaggcacagcgagaaggccgtgagccttgcgaacttgatacccgcgagtacgttgctggtgctccttacaccccagttgaacatgttgtgtttaacccttcgtctcgtgaccacattcagaagaaactccaagaggctgggtgggtcccgaccaagtacaccgataagggtgctcctgtggtggacgatgaggtactcgaaggagtacgtgtagatgaccctgagaagcaagccgctatcgacctcattaaagagtacttgatgattcagaagcgaatcggacagtctgctgagggagacaaagcatggcttcgttatgttgctgaggatggtaagattcatggttctgttaaccctaatggagcagttacgggtcgtgcgacccatgcgttcccaaaccttgcgcaaattccgggtgtacgttctccttatggagagcagtgtcgcgctgcttttggcgctgagcaccatttggatgggataactggtaagccttgggttcaggctggcatcgacgcatccggtcttgagctacgctgcttggctcacttca"

    seq2 = str2.upper()
    print("__________________________________________________________________________________________________________________________________")
    print("length of SeqA:",len(seq1))
    print("length of SeqA:",len(seq2))
    print("__________________________________________________________________________________________________________________________________\n\n")
    num_cores = multiprocessing.cpu_count()
    print("----------------------------------------------no. of cores-:", num_cores, "--------------------------------------------\n")
    pool = multiprocessing.Pool(processes=num_cores)
    results = []
    for i in range(num_cores):
        chunk_size = len(seq1) // num_cores
        start = i * chunk_size
        end = start + chunk_size
        if i == num_cores - 1:
            end = len(seq1)
        results.append(pool.apply_async(smith_waterman_parallel, (seq1[start:end], seq2)))
    pool.close()
    pool.join()
    scores = [result.get() for result in results]
    max_score = max(scores)
    print("Max score:", max_score)
    print("-----------------------------------------------END---------------------------------------------")

if __name__ == '__main__':
    main()
