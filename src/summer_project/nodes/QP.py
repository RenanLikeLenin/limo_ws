import numpy as np
from cvxopt.solvers import qp
from scipy.integrate import odeint
from cvxopt import matrix


class Robot:
    def __init__(self, u_min, u_max, phiRearEnd, phiLateral, deltaSafetyDistance, v_min, v_max):
        self.u_min = u_min
        self.u_max = u_max
        self.phiRearEnd = phiRearEnd
        self.phiLateral = phiLateral
        self.deltaSafetyDistance = deltaSafetyDistance
        self.v_min = v_min
        self.v_max = v_max

    def OCBF_SecondOrderDynamics(self, i, matrix_const, state, pfunc = print):
        ocpar = [-0.593787660013256, 1.41421356237309, 0, 0, 2.38168230431317, 1.68410370801184];
        c = np.array(ocpar)
        x0 = np.array(state)
        eps = 10
        psc = 0.1
        t = 0.1 * i

        # reference Trajectory
        vd = 0.5 * c[0] * t ** 2 + c[1] * t + c[2]
        u_ref = c[0] * t + c[1]

        # Physical Limitations on velocity
        b_vmax = self.v_max - x0[1]
        b_vmin = x0[1] - self.v_min

        # CLF
        phi0 = -eps * (x0[1] - vd) ** 2
        phi1 = 2 * (x0[1] - vd)

        def solveQP():

            A = np.array([[1, 0], [-1, 0], [phi1, -1], [1, 0], [-1, 0]])
            b = np.array([self.u_max, -self.u_min, phi0, b_vmax, b_vmin])

            # Rear-end Safety Constraints

            if matrix_const[0][0] != -1:
                xip = matrix_const[0][1]
                h = xip - x0[0] - self.phiRearEnd * x0[1] - self.deltaSafetyDistance
                vip = matrix_const[0][2]
                uminValue = abs(self.u_min)
                hf = h - 0.5 * (vip - x0[1]) ** 2 / uminValue

                if x0[1] <= vip or hf < 0:
                    p = 1
                    LgB = 1
                    LfB = 2 * p * (vip - x0[1]) + p ** 2 * h
                    A = np.append(A, [[LgB, 0]], axis=0)
                    b = np.append(b, [LfB])

                else:
                    LgB = self.phiRearEnd - (vip - x0[1]) / uminValue
                    LfB = vip - x0[1]
                    if LgB != 0:
                        A = np.append(A, [[LgB, 0]], axis=0)
                        b = np.append(b, [LfB + hf])

            # Lateral Safety Constraints

            for row_index, row in enumerate(matrix_const):
                if -1 in row:
                    continue
                else:
                    d1 = matrix_const[row_index][3]
                    d2 = state[row_index + 2]
                # L = state[row_index + 2] + state[0]
                L = 2.715

                v0 = matrix_const[row_index][2]

                bigPhi = self.phiLateral * x0[0] / L
                h = 0.1*(d2 - d1 - bigPhi * x0[1] - self.deltaSafetyDistance)

                uminValue = abs(self.u_min)
                hf = d2 - d1 - 0.5 * (v0 - x0[1]) ** 2 / uminValue - self.phiLateral * v0 * (
                        x0[0] + 0.5 * (x0[1] ** 2 - v0 ** 2) / uminValue) / L

                # if x0[1] <= v0 or hf < 0:
                LgB = bigPhi
                LfB = v0 - x0[1] - self.phiLateral * x0[1] ** 2 / L
                if LgB != 0:
                    stop = 1
                    A = np.append(A, [[LgB, 0]], axis=0)
                    b = np.append(b, [LfB + h])
                # else:
                #     LgB = self.phiLateral * v0 * x0[1] / uminValue / L - (v0 - x0[1]) / uminValue
                #     LfB = v0 - x0[1] - self.phiLateral * v0 * x0[1] / L
                #     if LgB != 0:
                #         A = np.append(A, [[LgB, 0]], axis=0)
                #         b = np.append(b, [LfB + hf])

            H = matrix([[1, 0], [0, psc]])
            f = matrix([[-u_ref], [0]]).trans()
            H = matrix(H, tc='d')
            f = matrix(f, tc='d')
            A = matrix(A, tc='d')
            b = matrix(b, tc='d')

            # opts = {'abstol' : 0.01, 'reltol' : 0.01, 'feastol' : 0.01}

            Solution = qp(H, f, A, b, options={
                'show_progress':False,
                'abstol' : 0.0001,
                'reltol' : 0.0001,
                'feastol' : 0.0001
                })
            # print(H)
            # print(f)
            # print(A)
            # print(b)
            # print(Solution)

            return Solution['x'].trans(), A, b

        def second_order_model(x, t, u):
            # global u, noise1, noise2
            dx = np.zeros(2)
            dx[0] = x[1]
            dx[1] = u

            return dx

        u, a, b = solveQP()
        au = np.array(a) @ np.array(u).T
        au_b = au + np.array(b)

        # x = np.zeros(2)
        # t_start = 0
        # t_end = 0.1
        # t_span = (t_start, t_end)

        # solution = odeint(second_order_model, x0[0:2], t_span, args=u)

        # rt = [solution[-1][0], solution[-1][1]]
        # print(u[0])
        if u is not None:
            return u[0], au_b
        else:
            return None, None


if __name__ == '__main__':
    my_robot = Robot(-10, 1, 0.18, 0.18, 0.1, 0, 1)
    L = 2.715
    d2 = 0.7
    d1 = 0.579
    out = my_robot.OCBF_SecondOrderDynamics(1, np.array([
    [-1, -1, -1, -1],
    [789, 0.96751131, 0, 0.91348869]
    ]),
    [1.30323824, 0.99, -1, 1.41176176])
        # [-1, -1, -1, -1],
        # [789, 0.96751131, 0, 0.91348869]
        # ]),
        # [1.30323824, 0.99, -1, 1.41176176])
    # print(out)
