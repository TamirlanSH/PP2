class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".","[.]")
    print(defangIPaddr(1, input()))