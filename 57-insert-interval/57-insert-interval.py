class Solution:
    # def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         res = []
        
#         for i in range(len(intervals)):
#             if newInterval[1] < intervals[i][0]:
#                 res.append(newInterval)
#                 return res + intervals[i:]
#             elif newInterval[0] > intervals[i][1]:
#                 res.append(intervals[i])
#             else:
#                 newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            
#         res.append(newInterval)
#         return res

  def insert(self, intervals, new_interval):
    merged = []
    for i in range(len(intervals)):
      interval = intervals[i]
      if new_interval[1] < interval[0]:
        merged.append(new_interval)
        return merged + intervals[i:]
      elif new_interval[0] <= interval[1]:
        new_interval = [min(interval[0], new_interval[0]), max(interval[1], new_interval[1])]
      else:
        merged.append(interval)

    merged.append(new_interval)

    return merged