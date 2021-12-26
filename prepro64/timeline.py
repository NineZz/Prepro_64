"""Concurrent Timeline"""

def main():
    """time"""
    second = int(input())
    minute = second//60
    hour = minute//60
    day = hour//24
    print("%02d:%02d:%02d:%02d"%(day, hour%24, minute%60, second%60))
main()
