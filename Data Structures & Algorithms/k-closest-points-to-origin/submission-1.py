class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res=[]
        maxHeap=[]
        for x,y in points:
            dist=-(x**2+y**2)
            heapq.heappush(maxHeap, [dist, x, y])
            if len(maxHeap)>k:
                heapq.heappop(maxHeap)
        while maxHeap:
            dist, x,y =heapq.heappop(maxHeap)
            res.append([x,y])
        return res



        # dis=[]
        # res=[]
        # for i in range(len(points)):
        #     dis.append((points[i][0])**2+(points[i][1])**2)
        # heapq.heapify(dis)
        # for i in range(len(points)):
        #     if ((points[i][0])**2+(points[i][1])**2)==dis[k-1]:
        #           res.append(points[i])
        # return res    

            