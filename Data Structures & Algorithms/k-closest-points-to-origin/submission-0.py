# skipping sqrt and subtracting 0, should be equivalent
def get_distance(point) -> int:
    return point[0]*point[0] + point[1]*point[1]

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.dist_to_point = {}
        self.distances = []
        self.points = points
        self.k = k
        top_k_points = []

        # calculate all of the distances
        for point in points:
            d = get_distance(point)
            self.distances.append(d)
            if d in self.dist_to_point.keys():
                self.dist_to_point[d].append(point)
            else:
                self.dist_to_point[d] = [point]
        
        # sort the distances
        self.distances.sort()

        # get the k min distances
        min_distances = self.distances[:k]

        # use dist mapping to get the topk points
        for min_d in min_distances:
            min_point = self.dist_to_point[min_d].pop(0)
            top_k_points.append(min_point)

        return top_k_points