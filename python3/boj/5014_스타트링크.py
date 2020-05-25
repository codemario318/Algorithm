from sys import stdin


if __name__ == '__main__':
    # F:층, S: 현재층 ,G:목적층, U:올라가는층수, D:내려가는층수
    #  (1 ≤ S, G ≤ F ≤ 1000000, 0 ≤ U, D ≤ 1000000)
    
    F, S, G, U, D = map(int,stdin.readline().split())
