bridge_lengths = 2, 100, 100
weights = 10, 100, 100
truck_weightss = [7,4,5,6], [10], [10,10,10,10,10,10,10,10,10,10]


for bridge_length, weight, truck_weights in zip(bridge_lengths, weights, truck_weightss):
    time = 0
    bridge = [0 for _ in range(bridge_length)]
    
    while len(bridge):
        time += 1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)

    print(time)
