class Hand:
    def __init__(self,cards,bid):
        self.cards = cards
        self.bid = bid
        self.type = 0
        self.score = 0
        self.order = 'AKQT98765432J'

    def determineType(self):
            
        for char in self.order:
            cardsNew = self.cards.replace('J', char)

            occurs = [0] * len(self.order)
            newtype = 0
            
            for c in cardsNew:
                n = self.order.find(c)
                occurs[n] = occurs[n] + 1
           
            
            #AAKQT
            if occurs.count(2) == 1:
                newtype = 1

            #AAKKQ
            if occurs.count(2) == 2:
                newtype = 2

            if 3 in occurs:
                #AAAKK
                if 2 in occurs:
                    newtype = 4
                    
                #AAAKQ
                else:
                    newtype = 3

            #AAAAK
            if 4 in occurs:
                newtype = 5

            #AAAAA
            if 5 in occurs:
                newtype = 6

            if newtype > self.type:
                self.type = newtype
                
    
    def calculateScore(self):
        base = len(self.order)

        self.score = self.score + (base**5) * self.type
        self.score = self.score + (base**4) * self.order[::-1].find(self.cards[0])
        self.score = self.score + (base**3) * self.order[::-1].find(self.cards[1])
        self.score = self.score + (base**2) * self.order[::-1].find(self.cards[2])
        self.score = self.score + (base**1) * self.order[::-1].find(self.cards[3])
        self.score = self.score + (base**0) * self.order[::-1].find(self.cards[4])


def main():
    f = open("day07/data.input", "r")
    Lines = f.readlines()

    hands = []

    for line in Lines:
        line = line.split(" ")
        hands.append(Hand(line[0], int(line[1])))

        hands[-1].determineType()
        hands[-1].calculateScore()


    Scores = [0] * len(hands)
    Bids = [0] * len(hands)

    for i in range(len(hands)):
        Scores[i] = hands[i].score
        Bids[i] = hands[i].bid


    zipped_lists = zip(Scores, Bids)

    sorted_pairs = sorted(zipped_lists)

    res = [[i for i, j in sorted_pairs],
       [j for i, j in sorted_pairs]]

    Bids = res[1]

    out = 0
    for i in range(len(Bids)):
        out = out + (i+1)*Bids[i]

    print(out)

if __name__ == '__main__':
    main()