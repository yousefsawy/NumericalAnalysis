# This error calculation method considers that the X points are equidistant.
def get_delta(data):
    return [data[i + 1] - data[i] for i in range(len(data) - 1)]


def get_error(a, b, Ys):
    delta = Ys

    if len(Ys) < 5:
        return 0
    else:
        for i in range(4):
            delta = get_delta(delta)

    sum_delta4 = sum(delta)

    error = ((sum_delta4 / len(delta)) * (b - a)) / 6480

    return error*-1