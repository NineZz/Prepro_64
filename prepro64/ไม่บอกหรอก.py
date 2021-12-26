"""ไม่บอกหรอกเกรดไปคำนวณเอาหยิ่ง"""
def main():
    """function grade"""
    score = int(input())
    grade = score >= 80 and 4.0 or \
        75 <= score <= 79 and 3.5 or \
            70 <= score <= 74 and 3.0 or \
                65 <= score <= 69 and 2.5 or \
                    60 <= score <= 64 and 2.0 or \
                        55 <= score <= 59 and 1.5 or \
                            50 <= score <= 54 and 1.0 or \
                                score <= 49 and 0.0
    print(grade)
main()
