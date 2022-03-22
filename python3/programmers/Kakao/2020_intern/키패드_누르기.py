KEYPAD = {
    1: (0, 0), 2: (0, 1), 3: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1), 9: (2, 2),
    '*': (3, 0), 0: (3, 1), '#': (3, 2), 
}

LEFT_HAND_KEY = {1, 4, 7, '*'}
RIGHT_HAND_KEY = {3, 6, 9, '#'}

LEFT = 'L'
RIGHT = 'R'

def solution(numbers, hand):
    fingerMoves = []
    leftFinger, rightFinger = KEYPAD['*'], KEYPAD['#']
    
    for number in numbers:
        if number in LEFT_HAND_KEY:
            fingerMoves.append(LEFT)
            leftFinger = KEYPAD[number]
            continue

        if number in RIGHT_HAND_KEY:
            fingerMoves.append(RIGHT)
            rightFinger = KEYPAD[number]
            continue

        destination = KEYPAD[number]
        
        leftFingerDist = calcL1Norm(leftFinger, destination)
        rightFingerDist = calcL1Norm(rightFinger, destination)
        useHand = None

        if leftFingerDist == rightFingerDist:    
            useHand, leftFinger, rightFinger = (LEFT, destination, rightFinger) if hand == 'left' else (RIGHT, leftFinger, destination)
        elif leftFingerDist < rightFingerDist:
            leftFinger = destination
            useHand = LEFT
        else:
            rightFinger = destination
            useHand = RIGHT

        fingerMoves.append(useHand)

    return ''.join(fingerMoves)

def calcL1Norm(pointA, pointB):
    aX, aY = pointA
    bX, bY = pointB

    dist = abs(aX - bX) + abs(aY - bY)

    return dist
