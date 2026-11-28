from Bio import SeqIO

# 1. NCBI Complete Record 읽기
record = SeqIO.read(
    "data/HBB_reference.gb",
    "genbank"
)

# 2. CDS 영역 찾기
cds_features = []

for feature in record.features:
    if feature.type == "CDS":
        cds_features.append(feature)

# 3. CDS 서열 추출
cds = cds_features[0].extract(record.seq)
reference = str(cds).upper()

# 4. 추출 결과 확인
print("유전자:", record.id)
print("CDS 길이:", len(reference))
print("CDS 시작:", reference[:3])
print("20번째 염기:", reference[19])
print("20번째 염기가 포함된 코돈:", reference[18:21])
print("앞부분 서열:", reference[:30])
