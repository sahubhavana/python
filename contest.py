import sys
from collections import defaultdict

input = sys.stdin.readline

# ------------------ INPUT ------------------
N, S, L = map(int, input().split())
M, K, P = map(int, input().split())

SP_PER_PLANE = S // P
OXC_PER_PLANE = M // P
R = N * SP_PER_PLANE * K

# ------------------ HELPERS ------------------

def oxc_port(group, spine, k, plane):
    """Compute OXC port index"""
    return group * SP_PER_PLANE * K + (spine % SP_PER_PLANE) * K + k

# ------------------ STATE ------------------

# OXC matchings (persist across queries)
# oxc_match[m][port] = connected_port or -1
oxc_match = [[-1] * R for _ in range(M)]

# ------------------ PROCESS QUERIES ------------------

for _ in range(5):
    Q = int(input())
    flows = [tuple(map(int, input().split())) for _ in range(Q)]

    # Desired connections per OXC
    desired = defaultdict(list)
    routes = []

    for (gA, lA, gB, lB) in flows:
        # Plane selection (simple)
        plane = (gA + gB) % P
        m = plane * OXC_PER_PLANE  # choose first OXC in plane

        # Spine selection
        spineA = plane * SP_PER_PLANE + (lA % SP_PER_PLANE)
        spineB = plane * SP_PER_PLANE + (lB % SP_PER_PLANE)

        kA = 0
        kB = 0

        pA = oxc_port(gA, spineA, kA, plane)
        pB = oxc_port(gB, spineB, kB, plane)

        desired[m].append((pA, pB))

        routes.append((spineA, kA, m, spineB, kB))

    # ------------------ UPDATE OXC MATCHINGS ------------------

    for m in range(M):
        used = set()
        new_match = oxc_match[m][:]

        # Keep existing valid connections
        for (u, v) in desired.get(m, []):
            if new_match[u] == v and new_match[v] == u:
                used.add(u)
                used.add(v)

        # Add missing connections
        for (u, v) in desired.get(m, []):
            if u in used or v in used:
                continue
            # Remove conflicts
            if new_match[u] != -1:
                old = new_match[u]
                new_match[old] = -1
                new_match[u] = -1
            if new_match[v] != -1:
                old = new_match[v]
                new_match[old] = -1
                new_match[v] = -1
            # Create new connection
            new_match[u] = v
            new_match[v] = u
            used.add(u)
            used.add(v)

        oxc_match[m] = new_match

    # ------------------ OUTPUT ------------------

    for m in range(M):
        print(" ".join(map(str, oxc_match[m])))

    for r in routes:
        print(*r)
