from Bio import SeqIO

# 1. FASTA 파일 읽기
record = SeqIO.read("data/sequence.fasta", "fasta")

# 2. 전체 염기서열 저장
sequence = str(record.seq).upper()

# 3. CDS 영역 추출 (51~494번)
reference = sequence[50:494]

# 4. 추출 결과 확인
print("유전자:", record.id)
print("전체 서열 길이:", len(sequence))
print("CDS 길이:", len(reference))
print("CDS 시작:", reference[:3])
print("20번째 염기:", reference[19])
print("해당 코돈:", reference[18:21])
