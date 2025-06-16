import java.util.*;

class Solution {

    private static final Point STAR = new Point(3, 0);
    private static final Point SHARP = new Point(3, 2);

    private static final Map<Integer, Point> KEYPAD = Map.ofEntries(
            entry(1, new Point(0, 0)), entry(2, new Point(0, 1)), entry(3, new Point(0, 2)),
            entry(4, new Point(1, 0)), entry(5, new Point(1, 1)), entry(6, new Point(1, 2)),
            entry(7, new Point(2, 0)), entry(8, new Point(2, 1)), entry(9, new Point(2, 2)),
            entry(0, new Point(3, 1))
    );

    private static final Set<Integer> LEFT_NUMBERS = Set.of(1, 4, 7);
    private static final Set<Integer> RIGHT_NUMBERS = Set.of(3, 6, 9);

    public String solution(int[] numbers, String hand) {
        Point left = STAR;
        Point right = SHARP;

        StringBuilder sb = new StringBuilder();

        for (int number : numbers) {
            Point target = KEYPAD.get(number);

            if (LEFT_NUMBERS.contains(number)) {
                sb.append('L');
                left = target;
            } else if (RIGHT_NUMBERS.contains(number)) {
                sb.append('R');
                right = target;
            } else {
                int leftDist = left.distanceTo(target);
                int rightDist = right.distanceTo(target);

                if (leftDist < rightDist || (leftDist == rightDist && "left".equals(hand))) {
                    sb.append('L');
                    left = target;
                } else {
                    sb.append('R');
                    right = target;
                }
            }
        }

        return sb.toString();
    }

    static class Point {
        final int row;
        final int col;

        Point(int row, int col) {
            this.row = row;
            this.col = col;
        }

        int distanceTo(Point other) {
            return Math.abs(this.row - other.row) + Math.abs(this.col - other.col);
        }
    }
}
