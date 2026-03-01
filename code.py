import pygame
import heapq
import time
import random
import math

pygame.init()

w, h = 1100, 700
window = pygame.display.set_mode((w, h), pygame.RESIZABLE)
pygame.display.set_caption("Pathfinding Simulator")

font_big = pygame.font.SysFont("Verdana", 22, bold=True)
font_txt = pygame.font.SysFont("Arial", 16)

white = (255,255,255)
black = (0,0,0)
grid_clr = (200,200,200)

vis_clr = (231,76,60)
open_clr = (241,196,15)
path_clr = (46,204,113)
src_clr = (52,152,219)
dst_clr = (155,89,182)
side_clr = (33,47,60)

size = 30

class spot:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.col = white
        self.next_nodes = []

    def show(self,surf,cell):
        pygame.draw.rect(surf,self.col,(self.y*cell,self.x*cell,cell,cell))
        pygame.draw.rect(surf,grid_clr,(self.y*cell,self.x*cell,cell,cell),1)

    def make_links(self,board):
        self.next_nodes = []
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx = self.x + dx
            ny = self.y + dy
            if 0 <= nx < size and 0 <= ny < size:
                if board[nx][ny].col != black:
                    self.next_nodes.append(board[nx][ny])

def calc_h(a,b,mode):
    if mode == "Manhattan":
        return abs(a[0]-b[0]) + abs(a[1]-b[1])
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def run_algo(draw_func,board,src,dst,algo_type,h_mode,info,dyn):
    idx = 0
    pq = []
    heapq.heappush(pq,(0,idx,src))

    backtrack = {}
    g_val = {cell:float("inf") for row in board for cell in row}
    g_val[src] = 0

    t0 = time.perf_counter()
    explored = 0

    while pq:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()

        node = heapq.heappop(pq)[2]
        explored += 1

        if node == dst:
            route = []
            while node in backtrack:
                route.append(node)
                node = backtrack[node]
                node.col = path_clr
            dst.col = dst_clr
            info["Visited"] = explored
            info["Cost"] = len(route)
            info["Time"] = f"{(time.perf_counter()-t0)*1000:.1f}ms"
            return True

        if dyn and random.random() < 0.1:
            rx = random.randint(0,size-1)
            ry = random.randint(0,size-1)
            block = board[rx][ry]
            if block not in [src,dst,node]:
                block.col = black

        for nxt in node.next_nodes:
            if nxt.col == black:
                continue

            new_g = g_val[node] + 1
            if new_g < g_val[nxt]:
                backtrack[nxt] = node
                g_val[nxt] = new_g

                h = calc_h((nxt.x,nxt.y),(dst.x,dst.y),h_mode)
                score = new_g + h if algo_type == "A*" else h

                idx += 1
                heapq.heappush(pq,(score,idx,nxt))

                if nxt != dst:
                    nxt.col = open_clr

        if explored % 2 == 0:
            draw_func()
            pygame.time.delay(10)

        if node != src:
            node.col = vis_clr

    return False
