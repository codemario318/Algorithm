import java.util.*;
import static java.util.Map.entry;

class Point {
    final int x;
    final int y;

    Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    @Override
    public boolean equals(Object obj) {
        if (!(obj instanceof Point)) return false;
        Point o = (Point) obj;
        return this.x == o.x && this.y == o.y;
    }

    @Override
    public int hashCode() {
        return Objects.hash(x, y);
    }
}

class Path {
    final Point from;
    final Point to;

    Path(Point a, Point b) {
        if (a.x < b.x || (a.x == b.x && a.y <= b.y)) {
            this.from = a;
            this.to = b;
        } else {
            this.from = b;
            this.to = a;
        }
    }

    @Override
    public boolean equals(Object obj) {
        if (!(obj instanceof Path)) return false;
        Path other = (Path) obj;
        return this.from.equals(other.from) && this.to.equals(other.to);
    }

    @Override
    public int hashCode() {
        return Objects.hash(from, to);
    }
}

class Solution {
    private static final int BOUND = 5;

    private static final Map<Character, Point> OFFSET = Map.ofEntries(
            entry('U', new Point(0, 1)),
            entry('D', new Point(0, -1)),
            entry('R', new Point(1, 0)),
            entry('L', new Point(-1, 0))
    );

    public int solution(String dirs) {
        Set<Path> visited = new HashSet<>();
        Point cur = new Point(0, 0);
        int answer = 0;

        for (char dir : dirs.toCharArray()) {
            Point offset = OFFSET.get(dir);
            Point next = new Point(cur.x + offset.x, cur.y + offset.y);

            if (!isInBounds(next)) continue;

            Path path = new Path(cur, next);

            if (!visited.contains(path)) {
                visited.add(path);
                answer++;
            }

            cur = next;
        }

        return answer;
    }

    private boolean isInBounds(Point p) {
        return p.x >= -BOUND && p.x <= BOUND && p.y >= -BOUND && p.y <= BOUND;
    }
}
