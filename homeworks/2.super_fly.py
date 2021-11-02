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

def delta_time(d, v, v2):
    return d/(v+v2)

def path(v, t):
    return v * t

def distances(d, v, v1, v2, e):
    if v < v1 or v < v2:
        return -1

    distances = []
    dt = delta_time(d, v, v2)
    sf = path(v,dt)
    i = 1
    while (d) >= e:
        distances.append(sf)
        d = d - path(v2, dt) - path(v1, dt)
        if i%2 == 0:
            dt = delta_time(d, v, v2)
        else:
            dt = delta_time(d, v, v1)
        i += 1
        sf = path(v,dt)

    return distances



if __name__ == '__main__':

    # d = int(input("d: "))
    # v = int(input("v: "))
    # v1 = int(input("v1: "))
    # v2 = int(input("v2: "))
    # e = int(input("e: "))

    d = 100
    v = 30
    v1 = 10
    v2 = 20
    e = 0.000001

    fly_distances = distances(d, v, v1, v2, e)

    total_distance = 0
    for i, dist in enumerate(fly_distances):
        total_distance += dist
        print(f"{i}: {dist:>23.23f}")

    print("Total distance: {}".format(total_distance))
