class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        #print(products)
        result = []
        i = 0
        j = 1
        while i < len(products) and j <= len(searchWord):
            if products[i][:j] == searchWord[:j]:
                temp = [products[i]]
                for k in range(1,3):
                    if i+k < len(products) and products[i+k][:j] == searchWord[:j]:
                        temp.append(products[i+k])
                result.append(temp)
                j += 1
            else:
                i += 1
        if i == len(products):
            while j <= len(searchWord):
                result.append([])
                j += 1
        return result