"""
Два града A и B са на разстояние d километра. В едно и също време от всеки град тръгва бърз влак в посока към другия.
Скоростта на влака тръгнал от град A е v1 км/ч, а скоростта на влака тръгнал от град B е v2 км/ч.
Едновременно с тръгването на влака от град А излита изключително бърза муха, която лети срещу влака тръгнал от град B
със скорост v км/ч. При срещата с този влак, мухата прави обратен завой и започва да лети към влака идващ от град А.
Когато го срещне, тя полетява в обратна посока и продължава така,
докато влаковете се срещнат (разстоянието между тях стане равно на дължината на  мухата  ɛ).
Да се напише програма, която по въведени от клавиатурата d, v, v1, v2 и ɛ, намира и отпечатва:
1) дължините на различните участъци от пътя, които мухата ще прелети;
2) общото разстояние, което ще прелети мухата.
"""

def delta_time(d, v, v1):
    """Calculates the time that the fly needs to meet the train"""
    return d/(v+v1)

def path(v, t):
    return v * t

def distances(d, v, v1, v2, e):

    if v < v1 or v < v2:
        return [], []

    distances = []
    dtimes = []
    dt = delta_time(d, v, v2)
    dtimes.append(dt)
    sf = path(v,dt)
    i = 1
    while (d) > e:
        distances.append(sf)
        d = d - path(v2, dt) - path(v1, dt)
        if i%2 == 0:
            dt = delta_time(d, v, v2)
        else:
            dt = delta_time(d, v, v1)
        i += 1
        dtimes.append(dt)
        sf = path(v,dt)

    return distances, dtimes

def print_result(distances):
    if distances:
        total_distance = 0
        header = "{:>3}: {:^26}".format("#", "Distances")
        print("\n" + header)
        for i in range(len(distances)):
            dist = distances[i]
            total_distance += dist
            print("{:>3}: {:>26.23f}".format(i, dist))
        l = len(header)
        total_distance_str ="Total distance: {}".format(total_distance)
        offset = (l - len(total_distance_str))
        print(" "*offset + total_distance_str )
    else:
        print("The fly is too small!")


def print_result1(distances, times):
    if distances and fly_times:
        total_distance = 0
        header = "{:>3}: {:^27} - {:^27}".format("#", "Distances", "Delta time")
        print("\n" + header)
        for i in range(len(distances)):
            dist = distances[i]
            time = times[i]
            total_distance += dist
            print("{:>3}: {:>27.23f} - {:>27.23f}".format(i, dist, time))
        l = len(header)
        total_distance_str ="Total distance: {}".format(total_distance)
        offset = (l - len(total_distance_str))
        print(" "*offset + total_distance_str )
    else:
        print("The fly is too small!")


if __name__ == '__main__':

    d = float(input("Distance between city A and city B (km):\nd =  "))
    v = float(input("Super Fly speed (km\h):\nv = "))
    v1 = float(input("Train A speed  (km\h):\nv1 = "))
    v2 = float(input("Train B speed  (km\h):\nv2 = "))
    e = float(input("The size of the super fly\ne = "))


    fly_distances, fly_times = distances(d, v, v1, v2, e)
    print_result(fly_distances)
    print()
    # print_result1(fly_distances,fly_times)

