import numpy as np


class NorthWest:
    def __init__(self, costs, demand, supply):
        self.price_lst = []
        self.a_cost = costs
        self.demand_list = demand
        self.supply_list = supply
        self.n = len(self.supply_list)
        self.m = len(self.demand_list)
        self.size_nm = self.n * self.m
        self.inf = 99999999999
        self.eps = 0.001
        for i in self.demand_list:
            i += self.eps / self.m
        self.supply_list[1] += self.eps
        self.route_array = [[0] * self.m for i in range(self.n)]
        self.dual_array = [[-1] * self.m for i in range(self.n)]
        self.north_west_method(self.n, self.m)
        self.pivot_n = -1
        self.pivot_m = -1
        while self.not_optimal(self.n, self.m):
            self.better_optimal()
            self.print_out()
        if len(self.price_lst) > self.size_nm:
            self.price_lst = self.price_lst[-self.size_nm:]
        if len(self.price_lst) == self.size_nm:
            self.price_lst = self.price_lst
        self.result_price = np.array(self.price_lst)
        self.result_costs = np.array(costs)
        self.result_costs.shape = (len(supply), len(demand))
        self.result_price.shape = (len(supply), len(demand))
        self.c = np.sum(self.result_price*self.result_costs)

    def return_plan(self):
        return self.result_price

    def return_c(self):
        return self.c

    def print_out(self):
        self.get_dual()
        for x in range(self.n):
            for y in range(self.m):
                if self.route_array[x][y] == 0:
                    self.price_lst.append(0)
                else:
                    self.price_lst.append(round(self.route_array[x][y]))

    def north_west_method(self, supply_size, demand_size):
        u = 0
        v = 0
        a_d = [0] * demand_size
        a_s = [0] * supply_size
        while u < supply_size and v < demand_size:
            if self.demand_list[v] - a_d[v] < self.supply_list[u] - a_s[u]:
                z = self.demand_list[v] - a_d[v]
                self.route_array[u][v] = z
                a_d[v] += z
                a_s[u] += z
                v += 1
            else:
                z = self.supply_list[u] - a_s[u]
                self.route_array[u][v] = z
                a_d[v] += z
                a_s[u] += z
                u += 1

    def not_optimal(self, size_n, size_m):
        n_max = -self.inf
        self.get_dual()
        for u in range(0, size_n):
            for v in range(0, size_m):
                x = self.dual_array[u][v]
                if x > n_max:
                    n_max = x
                    self.pivot_n = u
                    self.pivot_m = v
        return n_max > 0

    def get_dual(self):
        for u in range(0, self.n):
            for v in range(0, self.m):
                self.dual_array[u][v] = -0.5
                if self.route_array[u][v] == 0:
                    a_path = self.find_path(u, v)
                    z = -1
                    x = 0
                    for w in a_path:
                        x += z * self.a_cost[w[0]][w[1]]
                        z *= -1
                    self.dual_array[u][v] = x

    def find_path(self, u, v):
        a_path = [[u, v]]
        count = 0
        if not self.look_horizontally(a_path, u, v, u, v):
            count += 1
        return a_path

    def look_horizontally(self, a_path, u, v, u1, v1):
        for i in range(0, self.m):
            if i != v and self.route_array[u][i] != 0:
                if i == v1:
                    a_path.append([u, i])
                    return True
                if self.look_vertically(a_path, u, i, u1, v1):
                    a_path.append([u, i])
                    return True
        return False

    def look_vertically(self, a_path, u, v, u1, v1):
        for i in range(0, self.n):
            if i != u and self.route_array[i][v] != 0:
                if self.look_horizontally(a_path, i, v, u1, v1):
                    a_path.append([i, v])
                    return True
        return False

    def better_optimal(self):
        a_path = self.find_path(self.pivot_n, self.pivot_m)
        n_min = self.inf
        for w in range(1, len(a_path), 2):
            t = self.route_array[a_path[w][0]][a_path[w][1]]
            if t < n_min:
                n_min = t
        for w in range(1, len(a_path), 2):
            self.route_array[a_path[w][0]][a_path[w][1]] -= n_min
            self.route_array[a_path[w - 1][0]][a_path[w - 1][1]] += n_min
