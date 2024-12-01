class Solution:
    def maxPoints(self, points) :

        n = len(points)
        if n < 2:
            return n
        
        max_collinear = []
        
        for i in range(n):
            for j in range(i + 1, n):
                
                
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                collinear_points = [points[i], points[j]]
                
                for k in range(n):
                    if k == i or k == j:
                        continue
                    x3, y3 = points[k]
                    

                    if (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1):
                        collinear_points.append(points[k])
                
                
                if len(collinear_points) > len(max_collinear):
                    max_collinear = collinear_points
        
        return len(max_collinear)



            


        
        