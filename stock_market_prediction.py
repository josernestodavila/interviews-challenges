def predictAnswer(stockData, queries):
    cache = {}
    answers = []

    for query in queries:
        if query in cache:
            answers.append(cache[query])
        else:
            query_idx = query - 1
            stock_value = stockData[query_idx]
            left = stockData[:query_idx][::-1]
            right = stockData[query_idx + 1:]

            left_winner_idx = -1
            left_winner_distance = 0
            for i in range(len(left)):
                if left[i] < stock_value:
                    left_winner_idx = query_idx - i
                    left_winner_distance = i
                    break

            right_winner_idx = -1
            right_winner_distance = 0
            for i in range(len(right)):
                if right[i] < stock_value:
                    right_winner_idx = query + i
                    right_winner_distance = i
                    break

            if left_winner_idx < 0 and right_winner_idx < 0:
                winner_idx = -1
            elif left_winner_idx < 0 and right_winner_idx >= 0:
                winner_idx = right_winner_idx + 1
            elif left_winner_idx >= 0 and right_winner_idx < 0:
                winner_idx = left_winner_idx
            else:
                if left_winner_distance < right_winner_distance:
                    winner_idx = left_winner_idx
                elif left_winner_distance > right_winner_distance:
                    winner_idx = right_winner_idx + 1
                else:
                    winner_idx = left_winner_idx

            cache[query] = winner_idx
            answers.append(winner_idx)
    return answers
