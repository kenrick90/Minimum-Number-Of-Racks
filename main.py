
Height = int(input("Input Height\n"))

numberOfServers = int(input("Input Number Of Servers\n"))

servers = list(map(int,input("Input Servers\n").strip().split()))

maxPerRack=2

servers.sort(reverse=True)

print(servers)

racks=[[]]
heightTracker=[0]
numberTracker=[0]
rackOfInterest=0
i=0
while len(servers)>0:
    if (heightTracker[rackOfInterest] + servers[i]) <= Height \
        and (numberTracker[rackOfInterest] < maxPerRack):
            heightTracker[rackOfInterest] += servers[i]
            numberTracker[rackOfInterest] += 1
            racks[rackOfInterest].append(servers[i])
            servers.pop(i)
            i=0
    elif i == len(servers)-1:
        rackOfInterest+=1
        numberTracker.append(0)
        heightTracker.append(0)
        racks.append([])
        i=0
    else:
        i+=1
    if numberTracker[rackOfInterest]==2 or heightTracker[rackOfInterest]==Height:
        rackOfInterest+=1
        numberTracker.append(0)
        heightTracker.append(0)
        racks.append([])

    # print("servers are ", servers)
    # print("heighttracker", heightTracker)
    # print("numberTracker", numberTracker)
    # print("racks are ", racks)
    # print("rackOfInterest", rackOfInterest)
    # print("-----------------------------")

if numberTracker[rackOfInterest]==0:
    minimumNumber=rackOfInterest
else:
    minimumNumber=rackOfInterest+1

print("racks are ", racks)
print("rackOfInterest", rackOfInterest)
print("The minimum number of racks required are ", minimumNumber)

