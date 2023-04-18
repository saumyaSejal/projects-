

def smith_waterman(seq1, seq2, match_score=2, mismatch_score=-1, gap_penalty=-1):

    print("length of genome sequence A:",len(seq1))
    print("length of genome sequence B:",len(seq2))
    
    # initialize score matrix with zeros
    score_matrix = [[0 for _ in range(len(seq2)+1)] for _ in range(len(seq1)+1)]
    
    # initialize maximum score and position
    max_score = 0
    max_pos = None
    
    # fill in score matrix
    for i in range(1, len(seq1)+1):
        for j in range(1, len(seq2)+1):
            # calculate score for each possible alignment
            match = score_matrix[i-1][j-1] + (match_score if seq1[i-1] == seq2[j-1] else mismatch_score)
            delete = score_matrix[i-1][j] + gap_penalty
            insert = score_matrix[i][j-1] + gap_penalty
            
            # set score for current position as the maximum of the three scores
            score_matrix[i][j] = max(0, match, delete, insert)
            
            # update maximum score and position
            if score_matrix[i][j] > max_score:
                max_score = score_matrix[i][j]
                max_pos = (i, j)
    
    # traceback to find alignment
    aligned_seq1 = ""
    aligned_seq2 = ""
    i, j = max_pos
    while score_matrix[i][j] != 0:
        if score_matrix[i][j] == score_matrix[i-1][j-1] + (match_score if seq1[i-1] == seq2[j-1] else mismatch_score):
            aligned_seq1 = seq1[i-1] + aligned_seq1
            aligned_seq2 = seq2[j-1] + aligned_seq2
            i -= 1
            j -= 1
        elif score_matrix[i][j] == score_matrix[i-1][j] + gap_penalty:
            aligned_seq1 = seq1[i-1] + aligned_seq1
            aligned_seq2 = "-" + aligned_seq2
            i -= 1
        else:
            aligned_seq1 = "-" + aligned_seq1
            aligned_seq2 = seq2[j-1] + aligned_seq2
            j -= 1
    print(max_score)
    print(aligned_seq1)
    print(aligned_seq2)
    return max_score, aligned_seq1, aligned_seq2

# s1="AGTGTTAGAGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGCGC"
# s2="AGCGCGCGCGCGCGCGCG"

# smith_waterman(s1,s2)