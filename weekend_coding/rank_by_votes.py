import numpy as np
class Solution():
    def rankTeams(self, votes):
        len_votes = len(votes)
        if len_votes ==1:
            return votes
        sort_votes = np.sort(votes)
        print(sort_votes)
        characters = tuple(c_str for c_str in str(sort_votes[0]))

        vote_count =[]
        i=0
        j=0

        for j in range (0,len_votes):
            # 1, 2, 3
            i = 0
            for character in characters:
                # A, B, C
                for vote in votes:
                    count = [0] * len_votes
                    for i in range (0,len(characters)):
                        if  vote[i] == character:
                            count[i] += 1
                vote_count.append(count)
        print(vote_count)
def main():
    votes = ["ABC","ACB","ABC","ACB","ACB"]
    sol = Solution()
    sol.rankTeams(votes)

if __name__ == '__main__':
    main()