# A=int(input("수 입력: "))
# sum1=0
# sum2=0
# for i in range(1,A+1):
#     if i%2==0:
#         sum1+=i
#     else:
#         sum2+=i
# print(sum1)
# print(sum2)

# A=int(input("수 입력: "))
# cnt=0
# for i in range(1,A+1):
#     if(i%3==0):
#         print(i)
#         cnt+=1
# print(cnt)

# li=['D','A','B','C']
# for i in range(20,51):
#     print(li[i%4])


# for i in range(2000,2301):
#     if(i%4==0):
#         if(i%100!=0):
#             print(i,"윤년입니다.")
#     if(i%400==0):
#         print(i,"윤년입니다.")
#     else:
#         pass

# A=int(input("수 입력: "))
# cnt=0
# for i in range(1,A+1):
#     if(i%2==0):
#         cnt+=1
#         print(i)
# print(cnt)

# A=int(input("수 입력: "))
# sum=0
# for i in range(1,A+1):
#     if i%7==0:
#         sum+=i
# print(sum)

# A=int(input("수 입력: "))
# cnt3=0
# cnt5=0
# for i in range(1,A+1):
#     if i%3==0:
#         cnt3+=1
#     if i%5==0:
#         cnt5+=1
# print(cnt3-cnt5)

# li=['O', 'O', 'O', 'O', 'AB', 'B', 'A', 'A', 'O', 'AB', 'B', 'A', 'B', 'AB', 'AB', 'AB', 'O', 'A', 'A', 'AB', 'B', 'AB', 'O', 'B', 'A', 'O', 'A', 'O', 'AB', 'O', 'AB', 'AB', 'O', 'B', 'B', 'O', 'O', 'AB', 'B', 'A']
# print("A: ",li.count('A'))
# print("B: ",li.count('B'))
# print("O: ",li.count('O'))
# print("AB: ",li.count("AB"))

# count=0
# li = [6600, 4800, 3400, 3200, 4500, 5500, 3200, 7800, 4200, 5300, 7500, 4200, 7200, 5600, 6700, 8000, 7000, 6700, 6200, 6100, 4700, 7200, 7100, 5700, 5900, 4300, 5200, 5600, 5900, 6600, 4900, 5800, 7100, 5800, 4500, 3200, 7800, 5300, 7200, 8000]
# for i in li:
#     if i<=5000:
#         count+=1
# print(count)

# li=[80, 70, 44, 66, 40, 80, 77, 57, 68, 90, 75, 84, 99, 52, 45, 53, 54, 96, 59, 47, 57, 68, 74, 68, 79, 60, 63, 67, 43, 100, 43, 54, 77, 59, 75, 60, 97, 47, 100, 54]
# cnt=0
# for i in range(len(li)):
#     if li[i]<80:
#         cnt+=1
# print(cnt)

# li=[3466, 4777, 5484, 5652, 2539, 2766, -5299, 5616, -4556, 3308, 2872, 4152, -3555, 2925, -2977, 4658, 5715, -2965, 2267, 4997, 5175, 4662, 2278, 2961, 3155, 4359, 3990, 3096, 5716, 3990, -3879, 2829, -5671, 5343, 3929, -2295, -3298, 2621, -2028, 3575, -2697, 3526, 3399, 5126, 5821, 5697, -2029, -3875, 5165, -5092, 2656, -5445, 3422, 3317, 2929, 2865, 5557, 4577, 3608, -3533, 2725, 3106, 2564, 3036, 5608, -3586, -4713, 5875, 4993, 5438, 2191, -2272, -4397, 3233, 2557, 3612, 2156, 2372, -3131, 2700, -2152, 4787, -3383, 2182, 3429, 2620, 3502, 3946, 3473, 5863, -4063, 4008, 4814, 5089, 5988, -2562, 3062, -2316, 5108, 2789]
# sum=0
# for i in range(len(li)):
#     if li[i]<0:
#         li[i]=-li[i]
#     sum+=li[i]
# print(sum)

# A=int(input("단 입력: "))
# for i in range(1,10):
#     print(A,'*',i,'=',A*i)

# A=int(input("수 입력: "))
# if A%2==0:
#     print("짝수")
# else :
#     print("홀수")

# for i in range(1,5):
#     A=int(input("수 입력: "))
#     if A%2==0:
#         print(A,"는 짝수")
#     else:
#         print(A,"는 홀수")

# li=[]
# for i in range(1,5):
#     A=int(input("수 입력: "))
#     li.append(A)
# for i in range(0,5):
#     if li[i]%2==0:
#         print(li[i],"는 짝수")
#     else:
#         print(li[i],"는 홀수")

# for i in range(5):
#     A=int(input("수 입력"))
#     B=int(input("수 입력"))
#     if (A%10)+(B%10)>=10:
#         print("받아올림 발생")
#     else:
#         print("받아올림 발생하지 않음")

# li=[]
# for i in range(5):
#     A=int(input("수 입력: "))
#     li.append(A)
# print("5 과목의 평균은",sum(li)/5)
# for i in range(5):
#     if li[i]<=sum(li)/5:
#         print(li[i],"는 평균이하")

# sum=0
# li=[2585, 6241, 6088, 886, 144, 5847, 3600, 1764, 8281, 1345, 81, 8649, 2401, 10000, 7569, 7225, 3712, 9216, 9679, 9216, 484, 2209, 9849, 4661, 4489, 2809, 2304, 4561, 8649, 529, 8836, 361, 4225, 856, 6724, 196, 3364, 2401, 10000, 3600, 900, 5565, 3136, 841, 1296, 256, 3481, 4761, 3721, 7921, 8986, 3721, 676, 810, 81, 7553, 3025, 121, 2750, 5140, 2809, 4356, 1521, 8453, 484, 3364, 1764, 7191, 1296, 8649, 8464, 1369, 5625, 4096, 81, 5015, 324, 729, 49, 1225, 6606, 1296, 784, 1600, 9025, 729, 7542, 576, 4489, 2809, 4225, 1681, 1296, 81, 977, 4, 8579, 8841, 4761, 6978, 5476, 2472, 5476, 7923, 25, 441, 3025, 6724, 2304, 10000, 2916, 4900, 6241, 81, 5476, 5329, 2916, 2293, 5520, 2833, 9143, 784, 2500, 4508, 6385, 25, 289, 7569, 144, 169, 7225, 8582, 2725, 400, 3249, 6530, 676, 6400, 4900, 2081, 2800, 1296, 361, 1024, 9, 9801, 2601, 841, 1936, 400, 5184, 6211, 7921, 225, 784, 8147, 529, 1936, 6724, 4356, 4096, 3931, 3144, 8649, 225, 25, 256, 81, 729, 8115, 8100, 9409, 256, 2401, 3721, 5079, 6395, 256, 8464, 324, 3853, 7570, 1681, 4552, 5250, 4489, 8168, 196, 6724, 6875, 7600, 1761, 10000, 4356, 625, 1600, 256, 7225, 6561, 1444, 8281, 361, 961, 6889, 5878, 2809, 841, 625, 64, 3721, 676, 1, 5041, 784, 25, 1369, 2048, 1765, 484, 8867, 3844, 4225, 8281, 2025, 1635, 4077, 3481, 625, 961, 4, 3136, 400, 4356, 4356, 7396, 1444, 5776, 196, 7396, 2704, 676, 8140, 144, 2304, 6084, 6784, 1024, 196, 8649, 169, 5184, 1, 5929, 3481, 10000, 7056, 5041, 6084, 7093, 2601, 3844, 4362, 3844, 4356, 5197, 2601, 6780, 5041, 5625, 1369, 4356, 2673, 3721, 2304, 3721, 5476, 784, 7569, 6241, 9999, 36, 2589, 4900, 1849, 1156, 1936, 7926, 1089, 919, 64, 5428, 5372, 4356, 1936, 1681, 7569, 484, 7921, 400, 676, 2704, 3136, 7741, 5329, 7171, 9025, 400, 7845, 2401, 2025, 2809, 1849, 7389, 8649, 3714, 36, 196, 121, 1920, 1024, 6400, 4056, 5184, 1681, 4130, 7625, 729, 6561, 7225, 409, 4225, 6241, 625, 8359, 400, 9, 9025, 5041, 8836, 4761, 8649, 1937, 400, 81, 2510, 484, 6241, 729, 6853, 25, 2601, 9466, 2401, 2431, 5041, 3136, 10000, 2401, 6084, 256, 3516, 1089, 2601, 6543, 3249, 5675, 5184, 25, 7921, 6084, 1296, 4096, 6722, 5776, 81, 6241, 9801, 6125, 5776, 9084, 400, 121, 196, 4900, 9216, 7056, 7396, 1089, 8100, 230, 2401, 9280, 5586, 6670, 6724, 8281, 1444, 3600, 4, 955, 6888, 9409, 2401, 1156, 4900, 7056, 6889, 5476, 9409, 8874, 900, 8649, 5625, 5476, 900, 1521, 5367, 9, 3969, 8696, 2601, 256, 4763, 1089, 144, 8464, 7056, 3136, 1296, 576, 4594, 225, 2304, 5625, 1369, 1764, 625, 4619, 1764, 9025, 1521, 6561, 8464, 841, 2704, 3976, 1444, 576, 750, 3721, 7569, 144, 2362, 4548, 3136, 10000, 4667, 6400, 9216, 576, 1681, 1444, 961, 9, 2916, 441, 3364, 2494, 2916, 1, 7676, 7225, 1444, 484, 4096, 7921, 5329, 4624, 3844, 5429, 64, 6548, 8427, 9409, 2654, 81, 3136, 6241, 1764, 5596, 1841, 6206, 196, 324, 5041, 4900, 289, 36, 5913, 196, 2704, 2304, 7242, 144, 7569, 3284, 6241, 1791, 7921, 6484, 4096, 7569, 225, 196, 144, 8281, 4225, 3600, 1681, 7490, 5323, 1936, 9551, 2756, 7603, 3136, 3721, 5929, 5476, 1764, 324, 121, 1024, 2704, 7744, 8649, 841, 3136, 8836, 466, 4156, 6400, 841, 1089, 3969, 4235, 5329, 874, 49, 3844, 8649, 4624, 8281, 7882, 4356, 5986, 332, 9604, 2401, 4951, 3481, 9594, 4954, 7984, 576, 3721, 5776, 1, 2304, 3364, 2118, 1024, 1, 1849, 7529, 6233, 1602, 441, 5336, 8281, 3091, 4747, 4667, 5913, 900, 4489, 1, 3136, 361, 961, 4356, 7056, 6241, 2089, 5184, 8692, 7618, 25, 225, 49, 625, 1296, 1498, 6400, 4761, 9216, 291, 7396, 4761, 1225, 3721, 2209, 6724, 5329, 10000, 4, 64, 4062, 2193, 2938, 81, 196, 900, 1296, 9982, 529, 1369, 4489, 1936, 1225, 6044, 230, 4782, 7744, 6400, 5024, 400, 121, 8100, 1024, 1681, 7744, 8413, 6724, 1089, 196, 2209, 25, 841, 4489, 4761, 5498, 324, 1296, 6584, 289, 7396, 1600, 49, 3844, 6331, 4489, 9216, 3025, 1928, 3249, 4900, 8827, 3844, 6516, 7373, 662, 9971, 144, 3969, 7225, 8464, 9978, 1764, 2916, 4761, 6131, 961, 2025, 2915, 9328, 2029, 361, 3364, 2025, 2209, 3227, 2192, 8100, 2304, 841, 10000, 8836, 1024, 5476, 7744, 4428, 1156, 144, 4900, 4, 3600, 4664, 4900, 5625, 49, 2704, 158, 6084, 121, 1681, 930, 2500, 25, 2116, 6561, 49, 4489, 5666, 2601, 5341, 6084, 4356, 3969, 841, 9604, 400, 144, 1248, 1089, 2500, 5929, 3467, 1681, 9262, 3025, 441, 729, 9, 225, 441, 7828, 9409, 694, 625, 1521, 2129, 8890, 1296, 225, 9025, 2304, 9025, 7225, 9801, 9409, 25, 4085, 2401, 2225, 4761, 961, 4624, 5184, 9, 8464, 8464, 9689, 2106, 6703, 4096, 6561, 4, 1215, 9, 3249, 2500, 961, 9025, 16, 8649, 10000, 2809, 2916, 6093, 9091, 1849, 2916, 9, 4096, 4629, 6400, 1521, 5329, 5336, 8459, 5625, 4489, 576, 2116, 225, 3866, 2282, 1764, 10000, 9025, 1296, 2916, 1764, 196, 1089, 16, 6440, 7358, 8281, 4900, 25, 9216, 8374, 112, 1062, 400, 1, 6084, 2704, 1521, 529, 2862, 6889, 6724, 3249, 3364, 784, 2025, 400, 1849, 1089, 2601, 5184, 3721, 5329, 7056, 2140, 7396, 1820, 4356, 5377, 400, 8836, 9, 6767, 3025, 841, 100, 9097, 273, 1296, 1764, 4849, 4096, 1024, 8464, 9025, 576, 7744, 1849, 1369, 1444, 361, 324, 3481, 2304, 49, 5184, 2338, 576, 8237, 1936, 1202, 1764, 2401, 6724, 9025, 625, 4041, 4225, 6678, 7921, 7711, 3249, 1521, 3136, 7744, 361, 8649, 9801, 1610, 2704, 16, 2704, 1849, 4489, 25, 529, 817, 7744, 9877, 25, 8323, 6088, 8208, 7560, 3600, 7225, 3969, 8302, 2304, 36, 784, 2209, 7569, 2512, 576, 10000, 9025, 5041, 225, 2025, 121, 2500, 7569, 900, 1681, 5625, 5329, 7921, 169, 1314, 9635, 961, 5476, 625, 361, 324, 9625, 2500, 4096, 2487, 6561, 4225, 676, 441, 225, 9604, 529, 625, 10000, 441, 1521, 484, 5807, 9801, 3481, 2704, 6921, 9409, 1849, 2313, 1296, 2916, 9441, 1537, 7396, 6346, 2500, 1296, 2545, 4096, 3600, 1764, 676, 16, 2601, 441, 6084, 3249, 361, 4, 10002, 4356, 9156, 6889, 5900, 1631, 36]
# for i in li:
#     if((i**0.5)-int(i**0.5)==0.0):
#         sum+=i
# print(sum)

# for i in "hello":
#     print(i)

score=0
A=input("ox를 입력하세요: ")
for i in range(len(A)):
    if A[i]=='o' and A[i+1]=='o':
        score+=2**i
    if A[i]=='o' and A[i+1]=='x':
        score+=0
        i=0;
print(score)


# A=int(input("숫자 입력하세요: "))
# li=[]
# for i in range(1,A//2+1):
#     if A%i==0:
#         li.append(i)
# li.append(A)
# print(li)

# A=int(input("숫자 입력하세요: "))
# B=int(input("숫자 입력하세요: "))
# li=[]
# if A>B:
#     for i in range(1,B+1):
#         if B%i==0 and A%i==0:
#             li.append(i)
# else:
#     for i in range(1,A+1):
#         if A%i==0 and B%i==0:
#             li.append(i)
# print(li)

# A=int(input("숫자 입력하세요: "))
# li=[]
# for i in range(1,A+1):
#     if A%i==0:
#         li.append(i)
# if len(li)==2:
#     print("소수")
# else:
#     print("소수 아님")

# A=int(input("숫자 입력하세요: "))
# li=[]
# for i in range(1,A//2+1):
#     if A%i==0:
#         li.append(i)
# if sum(li)==A:
#     print(A)
# else :
#     print("완전수 아닙니다.")