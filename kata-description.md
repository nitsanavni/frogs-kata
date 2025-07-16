The Frog Date Kata


Objective:


Determine if two frogs jumping westward on an equator can meet at the same point at the same time, and if so, find the minimum number of jumps for them to meet.


Scenario:


Two frogs, Apollo and Bubbles, start at different points on an equator and jump westward. They have different jump distances but jump at the same time intervals (once per second). The equator is a circle, so jumps beyond its length wrap around the circle.


Description:
Apollo and Bubbles start from different points on an equator.
They are both jumping westward (in the same direction) and hope to meet each other.
The latitude line they are on forms a complete circle (equator), meaning that if either frog jumps past the westernmost point, it will loop back around to the easternmost point.
Apollo starts at position x1, and Bubbles starts at position x2 on this circular line.
Apollo can jump a fixed distance of v1 meters per jump, while Bubbles jumps v2 meters per jump.
Both frogs jump once per second.
Challenge:
1) Determine if the two frogs can land at the same point at the same time.
2) If they can meet, determine the minimum number of jumps it will take.
If they cannot meet at the same point at the same time, output Impossible.
Important Notes:
The equator has a total length of totalLength meters. Any jump that goes beyond totalLength meters will wrap around to the starting position.
The frogs can only meet if they land on the same exact point on the circle at the same time.


